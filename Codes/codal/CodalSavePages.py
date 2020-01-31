from bs4 import BeautifulSoup
import requests.packages.urllib3
import jsons
import time
from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import urllib.request

#requests.packages.urllib3.disable_warnings()

def getTitle(soup):
    columnTitles=[]
    table = soup.find('table', attrs={'class':'rayanDynamicStatement'})
    if (table):
        table_body = table.find('thead')
        rows = table_body.find_all('tr')


        cols = rows[0].find_all('th')
        siblingCols = rows[1].find_all('th')

        siblingCounter=0
        for col in cols:
            span = col.find('span')
            title = span.get_text(strip=True, separator=',').replace("\n", "")
            if (col.attrs["rowspan"]=="1"):   ## get second Title row for rowspan One, columne
                title = title + " " + siblingCols[siblingCounter].find_all('span')[0].contents[0].replace("\n", "").strip()
                siblingCounter+=1
            columnTitles.append(title)
    else:
        divBody = soup.find('div', attrs={'class':'table_wrapper'})
        table_body = divBody.find('table')
        body = table_body.find('tbody')
        row = body.find('tr')
        cols = row.find_all('th')
        for col in cols:
            span = col.find('span')
            title = span.get_text(strip=True, separator=',').replace("\n", "")
            columnTitles.append(title)
    return columnTitles

def getDataTable(soup):
    dataTable=[]
    table = soup.find('table', attrs={'class':'rayanDynamicStatement'})
    if (table):
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            dataRow=[]
            for col in cols:
                span = col.find('span')
                if(span.contents==[]):
                    data = ""
                else:
                    data = persianStrToInt(span.get_text(strip=True, separator=',').replace("\n", ""))
                dataRow.append(data)
            dataTable.append(dataRow)
    else:
        divBody = soup.find('div', attrs={'class':'table_wrapper'})
        divBody2 = divBody.find('div')
        table_body = divBody2.find('table')
        body = table_body.find('tbody')
        rows = body.find_all('tr')
        for row in rows:
            if (row.attrs['class'][0]=='HiddenRow'):
                continue
            cols = row.find_all('td')
            dataRow=[]
            for col in cols:
                if (col.attrs['class'][0]=='Hidden'):
                    continue
                span = col.find('span')
                data = persianStrToInt(span.get_text(strip=True, separator=',').replace("\n", ""))
                dataRow.append(data)
            dataTable.append(dataRow)
    return dataTable

def gettheSubjectRecord(soup):
    select = soup.find('select', attrs={'id':'ddlTable'})
    optionData={}
    if (select):
        options = select.find_all('option')
        for option in options:
            value = option['value']
            text = option.get_text(strip=True, separator=',').replace("\n", "")
            optionData[text]=value
    return optionData

def saveListOfSoratHayeMaliToJson(table, chrome, url, title, tracingNo, symbol, companyName, sentDateTime):
    pageSource = chrome.loadURLByTrackingNoOffline(symbol, url, tracingNo, 1)
    soup = BeautifulSoup(pageSource,"lxml")
    try:
        theSubjectRecord=gettheSubjectRecord(soup)
        data={"TracingNo":tracingNo, "Title": title, "SentDateTime":sentDateTime, "Symbol":symbol, "CompanyName":companyName, \
              "theSubjectRecord":theSubjectRecord}
        table.insert(data)
    except:
        print(f'Error theSubjectRecord Comment: {err}') 

def saveSoratVaziatMaliToJson(table, chrome, url, sheetId, title, tracingNo, symbol, companyName, sentDateTime):
    pageSource = chrome.loadURLByTrackingNoOffline(symbol, url, tracingNo, sheetId)
    
def saveSodVaZianToJson(table, chrome, url, sheetId, title, tracingNo, symbol, companyName, sentDateTime):
    pageSource = chrome.loadURLByTrackingNoOffline(symbol, url, tracingNo, sheetId)
    
    soup = BeautifulSoup(pageSource,"lxml")
        
    try:
        titles=getTitle(soup)
        dataTable=getDataTable(soup)
        data={"TracingNo":tracingNo, "Title": title, "SentDateTime":sentDateTime, "Symbol":symbol, "CompanyName":companyName, \
              "TableTitle":titles, "dataTable":dataTable}
        table.insert(data)
    except Exception as err:
        print("Error In TrackingNo:"+str(tracingNo)+", Symbol:"+persianToFinglish(symbol))
        print(f'Error SodVaZianUrlToJson Comment: {err}') 

#TODO use group callback to traverse over data
#TODO extract list of SoratHaye mali from sod and zian
    
def updateCodalListOfSoratMali(chrome, symbol, codalRawDataTableName, sheetId):
    
    ## TrackNo_ValueNumber
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalLinks,'symbol':symbol}))
    LinkOfPagesTable = db.table('Links')
    LinkOfPages=LinkOfPagesTable.all()
    
    theLetterInLinkOfPages = []
    for linkOfPage in LinkOfPages:
        title=linkOfPage['letter']['Title']
        if (title.find("صورت‌های مالی")>-1):
            theLetterInLinkOfPages.append(linkOfPage)

    codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol}))
    theSubjectsTable = codalRawDataDB.table(codalRawDataTableName)

    theSubjectsTableData = theSubjectsTable.all()
    theSubjectsTableDataLen = len(theSubjectsTableData)
    linkOfPageCounter=0
    for linkOfPage in theLetterInLinkOfPages:
        if (len(theLetterInLinkOfPages)<=theSubjectsTableDataLen):
            break;
        isFind=False
        for theSubjectRecord in theSubjectsTable:
            if (theSubjectRecord['TracingNo']==linkOfPage['letter']['TracingNo']):
                isFind=True
                break
        if not (isFind):
            url = "https://www.codal.ir"+linkOfPage['letter']['Url']+"&sheetId="+str(sheetId)

            print(str(linkOfPageCounter)+"/"+str(len(theLetterInLinkOfPages)), end="\r", flush=True)

            saveListOfSoratHayeMaliToJson(theSubjectsTable, chrome, url, linkOfPage['letter']['Title'], linkOfPage['letter']['TracingNo']\
            , linkOfPage['letter']['Symbol'], linkOfPage['letter']['CompanyName'], linkOfPage['letter']['SentDateTime'])

            theSubjectsTableDataLen+=1
        linkOfPageCounter+=1
    codalRawDataDB.close()
 
def processSoratMali(chrome, theLetterInLinkOfPagesWithSheetID, codalRawDataDB, symbol, codalRawDataTableName, saveToJsonCallback):
    codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol}))
    theSubjectsTable = codalRawDataDB.table(codalRawDataTableName)

    theSubjectsTableData = theSubjectsTable.all()
    theSubjectsTableDataLen = len(theSubjectsTableData)
    linkOfPageCounter=0
    for linkOfPageWithSheetID in theLetterInLinkOfPagesWithSheetID:
        if (len(theLetterInLinkOfPagesWithSheetID)<=theSubjectsTableDataLen):
            break;
        linkOfPage=linkOfPageWithSheetID['linkOfPage']
        sheetId=linkOfPageWithSheetID['sheetId']
        isFind=False
        for theSubjectRecord in theSubjectsTable:
            if (theSubjectRecord['TracingNo']==linkOfPage['letter']['TracingNo']):
                isFind=True
                break
        if not (isFind):
            url = "https://www.codal.ir"+linkOfPage['letter']['Url']+"&sheetId="+str(sheetId)

            print(str(linkOfPageCounter)+"/"+str(len(theLetterInLinkOfPagesWithSheetID)), end="\r", flush=True)

            saveToJsonCallback(theSubjectsTable, chrome, url, sheetId, linkOfPage['letter']['Title'], linkOfPage['letter']['TracingNo']\
            , linkOfPage['letter']['Symbol'], linkOfPage['letter']['CompanyName'], linkOfPage['letter']['SentDateTime'])

            theSubjectsTableDataLen+=1
        linkOfPageCounter+=1

def updateCodalSoratMali(chrome, symbol):
    ## TrackNo_ValueNumber
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalLinks,'symbol':symbol}))
    LinkOfPagesTable = db.table('Links')
    LinkOfPages=LinkOfPagesTable.all()
    
    theLetterInLinkOfPages = []
    for linkOfPage in LinkOfPages:
        title=linkOfPage['letter']['Title']
        if (title.find("صورت‌های مالی")>-1):
            theLetterInLinkOfPages.append(linkOfPage)

    codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol}))
    soratMaliTableDataTable = codalRawDataDB.table('ListOfSoratHayeMali')
    soratMaliTableData = soratMaliTableDataTable.all()
    soratMaliTableDataLen = len(soratMaliTableData)
    
    linkOfPageCounter=0
    SoratMaliLetterGroupBySubjects = {}
    for linkOfPage in theLetterInLinkOfPages:
        for sorateMali in soratMaliTableData:
            if sorateMali['TracingNo']==linkOfPage['letter']['TracingNo']:
                for theSubjectKey in sorateMali['theSubjectRecord']:
                    sheetId = sorateMali['theSubjectRecord'][theSubjectKey]
                    if not (theSubjectKey in SoratMaliLetterGroupBySubjects):
                        SoratMaliLetterGroupBySubjects[theSubjectKey]=[]
                    SoratMaliLetterGroupBySubjects[theSubjectKey].append({'linkOfPage':linkOfPage, 'sheetId':sheetId})
    #----------------
    theSubjectKey='صورت وضعیت مالی'
    soratVaziatMali = SoratMaliLetterGroupBySubjects[theSubjectKey]  
    codalRawDataTableName='soratVaziatMali'
    processSoratMali(chrome, soratVaziatMali, codalRawDataDB, symbol\
        , codalRawDataTableName, saveSoratVaziatMaliToJson)
    #----------------
    theSubjectKey='صورت سود و زیان'
    soratVaziatMali = SoratMaliLetterGroupBySubjects[theSubjectKey]  
    codalRawDataTableName='SodVaZian'
    processSoratMali(chrome, soratVaziatMali, codalRawDataDB, symbol\
        , codalRawDataTableName, saveSodVaZianToJson)
    #----------------

    codalRawDataDB.close()

 
def doOperation(symbol, symbolIndex, symbolsCounter):
    #todo: extract co list name and create folder for them 
    ## TrackNo_ValueNumber
    print("------"+persianToFinglish(symbol['sy']))        
    chrome = Chrome(False)
    updateCodalListOfSoratMali(chrome, symbol['sy'], 'ListOfSoratHayeMali', 1)
    updateCodalSoratMali(chrome, symbol['sy'])
    del chrome
    print("\n"+str(symbolIndex)+'/'+str(symbolsCounter)+":"+"-----")

def updateCodalSavePages(start, end):
    timer = Timer()
    GroupProcess.getSymbols(start, end, True, doOperation)
    timer.printWatch()
    del timer
    