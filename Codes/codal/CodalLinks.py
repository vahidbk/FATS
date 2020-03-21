import requests
from bs4 import BeautifulSoup
import requests.packages.urllib3
import jsons
import time
from CommonDefs import *

def getLinkOfSymbol(symbol):
    requests.packages.urllib3.disable_warnings()
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalLinks,'symbol':symbol}))
    LinkOfPagesTable = db.table("Links")
    tempLinkOfPagesTable=LinkOfPagesTable.all()
    letterCounter=0
    letterCounter=len(LinkOfPagesTable)
    pageNumber=1
    breakDown=False
    while(True):
        try:
            url="https://search.codal.ir/api/search/v2/q?&Audited=true&AuditorRef=-1&Category=-1&Childs=false&CompanyState=0&CompanyType=-1&Consolidatable=true&IsNotAudited=false&Length=-1&LetterType=-1&Mains=true&NotAudited=true&Publisher=false&NotConsolidatable=true&Symbol="+symbol+"&PageNumber="+str(pageNumber)+"&TracingNo=-1&search=true"
            response = requests.get(url, verify = False, timeout=(10, 20))
        except Exception as err:
            print(f'Other error occurred: {err}') 
            ErrorJson=True
        else:
            ErrorJson=False

        internalCounter=0
        try:
            letters=[];
            codaldata = response.json()
            if not (codaldata["Letters"]):
                ErrorJson = True
            for letter in codaldata["Letters"]:
                if (letterCounter>=int(codaldata["Total"])):
                    breakDown = True
                isFind=False
                for letterInDB in tempLinkOfPagesTable:
                    if (letterInDB['letter']['TracingNo']==letter["TracingNo"]):
                        isFind=True
                        break
                if not (isFind):
                    letterCounter+=+1
                    internalCounter+=1
                    letters.append({'letter':letter})
        except:
            ErrorJson = True
            letter=[]

        LinkOfPagesTable.insert_multiple(letters)
        #LinkOfPagesTable.all()['letters']
        if ErrorJson:
            breakDown=True
            
        if (breakDown):
            break;
    
        print("          Page:" + str(pageNumber)+"/"+str(codaldata["Page"]), end="\r", flush=True)
        pageNumber=pageNumber+1
    print("")
    db.close()
    return

def updateCodalLetterLinks(start, end):
    groupDB = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
    symbolsTable = groupDB.table('Symbols')
    symbols = symbolsTable.all()
    symbolsCounter = len(symbols)
    timer = Timer()
    def doOperation(symbol, index, Count):
        print(str(index)+'/'+str(Count)+":"+persianToFinglish(symbol['sy'].strip()))
        getLinkOfSymbol((symbol['sy'].strip()))
    GroupProcess.getSymbols(start, end, True, doOperation)
            
    groupDB.close()
    timer.printWatch()
    del timer


#updateCodalLetterLinks(785,785)