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


def SodAndZianUrlToJson(table, chrome, url, title, tracingNo, symbol, companyName, sentDateTime):
    pageSource = chrome.loadURLByTrackingNoOffline(symbol, url, tracingNo, 1)
    
    soup = BeautifulSoup(pageSource,"lxml")
    try:
        titles=getTitle(soup)
        dataTable=getDataTable(soup)
        data={"TracingNo":tracingNo, "Title": title, "SentDateTime":sentDateTime, "Symbol":symbol, "CompanyName":companyName, \
              "TableTitle":titles, "dataTable":dataTable}
        table.insert(data)
    except Exception as err:
        print("Error In TrackingNo:"+str(tracingNo)+", Symbol:"+persianToFinglish(symbol))
        print(f'Error Comment: {err}') 

    
def updateCodalSavePages(start, end):
    chrome = Chrome(False)

    groupDB = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
    symbolsTable = groupDB.table('Symbols')
    symbols = symbolsTable.all()
    symbolsCounter = len(symbols)
    symbolIndex = 0;
    timer = Timer()

    #todo: extract co list name and create folder for them 
    ## TrackNo_ValueNumber

    for symbol in symbols:
        symbolIndex+=1
        if (start):
            if (symbolIndex<int(start)):
                continue
        if (end):
            if (symbolIndex>int(end)):
                continue
        print("------"+persianToFinglish(symbol['sy']))        
        if not (symbol['GroupName']=='Unknown' or symbol['st']==2 or symbol['st']==3):
            
            
            
            
            db = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalLinks,'symbol':symbol['sy']}))
            LinkOfPagesTable = db.table('Links')
            LinkOfPages=LinkOfPagesTable.all()
            codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol['sy']}))
            SodAndZianTable = codalRawDataDB.table('SodAndZian')
            
            SodAndZianLinkOfPages = []
            for linkOfPage in LinkOfPages:
                title=linkOfPage['letter']['Title']
                if (title.find("صورت‌های مالی")>-1):
                    SodAndZianLinkOfPages.append(linkOfPage)
            
            sodAndZianTableData = SodAndZianTable.all()
            sodAndZianTableDataLen = len(sodAndZianTableData)
            linkOfPageCounter=0
            for linkOfPage in SodAndZianLinkOfPages:
                if (len(SodAndZianLinkOfPages)<=sodAndZianTableDataLen):
                    break;
                isFind=False
                for sodAndZianData in sodAndZianTableData:
                    if (sodAndZianData['TracingNo']==linkOfPage['letter']['TracingNo']):
                        isFind=True
                        break
                if not (isFind):
                    url = "https://www.codal.ir"+linkOfPage['letter']['Url']+"&sheetId=1"
                    print(str(linkOfPageCounter)+"/"+str(len(SodAndZianLinkOfPages)), end="\r", flush=True)
                    SodAndZianUrlToJson(SodAndZianTable, chrome, url, linkOfPage['letter']['Title'], linkOfPage['letter']['TracingNo']\
                                        , linkOfPage['letter']['Symbol'], linkOfPage['letter']['CompanyName'], linkOfPage['letter']['SentDateTime'])
                    sodAndZianTableDataLen+=1
                linkOfPageCounter+=1
            codalRawDataDB.close()
        else:
            print("\n"+str(symbolIndex)+'/'+str(symbolsCounter)+":"+"-----")
            
    groupDB.close()
    timer.printWatch()
    del timer
    del chrome


#updateCodalSavePages(785,785)