from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime
                
#Todo:extract function for sod and zian
def tagGeneratorSozAndZian(symbol):
    codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol}))
    SodAndZianTable = codalRawDataDB.table('SodAndZian')
    
    sodAndZianTableData = SodAndZianTable.all()
    tagDataTable=[]
    for sodAndZianData in sodAndZianTableData:
        tracingNo=sodAndZianData["TracingNo"]
        pageTitle=sodAndZianData["Title"]
        symbol=sodAndZianData["Symbol"]
        companyName=sodAndZianData["CompanyName"]
        sentDateTime=sodAndZianData["SentDateTime"]
        tableTitle=sodAndZianData["TableTitle"]
        dataTable=sodAndZianData["dataTable"]
        
        #mergeRowTitle
        #merge
        #ignore zero data
        #extract date from (date and dore , normalized)
        
        #pageTitleExtraction

        pageTitleContent={'talfighi':False, 'duration':12, 'hesabrasi':False\
            , 'date':None, 'sendDate':None, 'sendTime':None, 'deltaDayToSendDate':None, }
        if (pageTitle.find("سال مالی")>-1):pageTitleContent['duration']=12
        #if (pageTitle.find("میاندوره‌ای")>-1):
        if pageTitle.find("۶ ماهه")>-1:pageTitleContent['duration']=6
        if pageTitle.find("۳ ماهه")>-1:pageTitleContent['duration']=3
        if pageTitle.find("۹ ماهه")>-1:pageTitleContent['duration']=9
        if pageTitle.find("حسابرسی نشده")>-1:pageTitleContent['hesabrasi']=False
        if pageTitle.find("حسابرسی شده")>-1:pageTitleContent['hesabrasi']=True
        if pageTitle.find("تلفیقی")>-1:pageTitleContent['talfighi']=True
        date=extractDateFromStr(pageTitle)
        sendDate=extractDateFromStr(sentDateTime)
        sendTime=extractTimeFromStr(sentDateTime)
        if date:pageTitleContent['date']=date
        if sendDate:pageTitleContent['sendDate']=sendDate
        if sendTime:pageTitleContent['sendTime']=sendTime
        if ((date!=None) & (sendDate!=None)):
            deltaDayToSendDate=JalaliDateTime(date['year'], date['month'], date['day'])\
                - JalaliDateTime(sendDate['year'], sendDate['month'], sendDate['day'])
            pageTitleContent['deltaDayToSendDate']=deltaDayToSendDate
        duration=pageTitleContent['duration']
        
        #firstRowContentsExtraction
        firstRowContents=[]
        for title in tableTitle:
            content={'sharh':False, 'edition':1, 'duration':pageTitleContent['duration'], 'hesabrasi':False, 'date':None }
            if title.find('شرح')>-1:content['sharh']=True
            if title.find('سال مالي')>-1:content['duration']=12
            if title.find('دوره منتهي')>-1:content['duration']=duration
            if title.find('دوره مشابه')>-1:content['duration']=duration
            if title.find("۶ ماهه")>-1:content['duration']=6
            if title.find("۳ ماهه")>-1:content['duration']=3
            if title.find("۹ ماهه")>-1:content['duration']=9
            if title.find('تجدید ارائه')>-1:content['edition']=2
            if title.find('حسابرسی شده')>-1:content['hesabrasi']=True
            if title.find("جهت ارائه به حسابرس")>-1:content['hesabrasi']=True
            date = extractDateFromStr(title)
            if(date):
                if (date['month']==12):
                    content['duration']=12
                content['date']=date
            firstRowContents.append(content)


        #dataTableCorrection
        correctedDataTable=[]
        superSubject=""
        for data in dataTable:
            subject=data[0]
            isSuperSubject=True
            rejectRow=True
            for index in range(1, len(data)-1):
                if data[index].strip()!="" and isSuperSubject==True:
                    isSuperSubject=False
                if not(data[index].strip()=="" or data[index]=="0") and rejectRow==True:
                    rejectRow=False
            if subject.find("دوره منتهی")>-1:
                continue
            if (isSuperSubject):
                superSubject=subject
                continue
            elif (rejectRow==True):
                continue
            if (subject==""):
                subject="جمع "+superSubject;
            correctedData=[[superSubject, subject]]
            for index in range(1, len(data)-1):
                correctedData.append(data[index])
            correctedDataTable.append(correctedData)
        
        #tagDataGeneration
        for correctedData in correctedDataTable:
            for index  in range(1, len(firstRowContents)-1):
                tagDic={}
                tagDic['letter']=tracingNo
                tagDic['pageTitle']=pageTitle
                tagDic['letterName']="SodAndZian"
                tagDic['symbol']=symbol
                tagDic['superSubject']=correctedData[0][0]
                tagDic['Subject']=correctedData[0][1]
                tagDic['value']=correctedData[index]
                tagDic['edition']=firstRowContents[index]['edition']
                tagDic['duration']=firstRowContents[index]['duration']
                tagDic['hesabrasi']=firstRowContents[index]['hesabrasi']
                tagDic['date']=firstRowContents[index]['date']
                #tagDic['talfighi']=pageTitleContent['talfighi']
                #tagDic['date']=pageTitleContent['date']
                tagDic['sendDate']=pageTitleContent['sendDate']
                tagDic['sendTime']=pageTitleContent['sendTime']
                if (tagDic['date']==pageTitleContent['deltaDayToSendDate']):
                    tagDic['deltaDayToSendDate']=pageTitleContent['deltaDayToSendDate']
                if (tagDic['date']):
                    if (tagDic['value']):
                        if (tagDic['value']!="0"):
                            tagDataTable.append(tagDic)
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.TagData,'symbol':symbol}))
    db.purge_table("Main")
    table = db.table("Main")
    table.insert_multiple(tagDataTable)
    db.close()
