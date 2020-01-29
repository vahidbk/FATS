import os
from selenium import webdriver
from tinydb import TinyDB, Query
from tinydb import where
from enum import Enum
from datetime import datetime
#import finglish

def extractDateFromStr(str):
    try:
        eslash1 = str.find("/")   
        eslash2 = str.find("/", eslash1+1)   
        if (eslash2-eslash1!=3):
            return
        year=int(str[eslash1-4:eslash1])
        month=int(str[eslash1+1:eslash1+3])
        day=int(str[eslash2+1:eslash2+3])
    except Exception as err:
        return
    return {'year':year, 'month':month, 'day':day}

def extractTimeFromStr(str):
    try:
        donoghte1 = str.find(":")   
        donoghte2 = str.find(":", donoghte1+1)   
        if (donoghte2-donoghte1!=3):
            return
        hour=int(str[donoghte1-2:donoghte1])
        minute=int(str[donoghte1+1:donoghte1+3])
        second=int(str[donoghte2+1:donoghte2+3])
    except Exception as err:
        return
    return {'hour':hour, 'minute':minute, 'second':second}
    
# createDirectory("test/ttt/ss")
def createDirectory(path):
    folders = path.split("/")
    currentPath=""
    for folder in folders:
        if (currentPath==""):
            currentPath=folder
        else:
            currentPath=currentPath+'/'+folder
        try:
            os.mkdir(currentPath)
        except OSError:
            pass
    return path

#FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol['sy']})
class FilenameManager(Enum):
    Temp=0
    CodalLinks = 1
    Groups = 2
    CodalRawData = 3
    TagData = 4
    CatchHTML = 5
    LoginData = 6
    def get(params):
        value=params['enum']
        if value==FilenameManager.Temp:result=params['filename']
        elif value==FilenameManager.CodalLinks:result=createDirectory('DB/Symbols/'+params['symbol']+"/")+'CodalLinks.json'
        elif value==FilenameManager.Groups:result=createDirectory('DB/General/')+'Groups.json'
        elif value==FilenameManager.CodalRawData:result=createDirectory('DB/Symbols/'+params['symbol']+"/")+'CodalRawData.json'
        elif value==FilenameManager.TagData:result=createDirectory('DB/Symbols/'+params['symbol']+"/")+'TagData.json'
        elif value==FilenameManager.CatchHTML:result=createDirectory('DB/Symbols/'+params['symbol']+"/CatchHTML/") + ("tracingNo"+str(params['tracingNo'])+"_"+str(params['value'])+".html")
        elif value==FilenameManager.LoginData:result=createDirectory('ImportantDatas/') + 'LoginData.json'
        else: result=createDirectory("../dumpFolder")+"dumpfile"
        return result
# "\033[F" – move cursor to the beginning of the previous line
# "\033[A" – move cursor up one line

def persianStrToInt(string):
    return string.replace(',','').replace('۰','0').replace(')','')\
           .replace('-','').replace('(','-').replace('۱','1').replace('۲','2')\
           .replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6')\
           .replace('۷','7').replace('۸','8').replace('۹','9')    

def persianToFinglish(string):
    persian2FinglishDic={'ض':'z','ص':'s','ث':'s','ق':'gh','ف':'f','غ':'gh',\
    'ع':'e','ه':'h','خ':'kh','ح':'h','ج':'j','چ':'ch','پ':'p','ش':'sh',\
        'س':'s','ی':'i','ب':'b','ل':'l','ا':'a','ت':'t','ن':'n','م':'m',\
            'ک':'k','گ':'g','ظ':'z','ط':'t','ز':'z','ر':'r','ذ':'z','د':'d',\
                'ئ':'i','و':'v','ة':'h','ژ':'zh','إ':'a','أ':'a','ء':'a','ۀ':'a',\
                    'آ':'a','۰':'0','۲':'2','۳':'3','۴':'4','۵':'5','۶':'6',\
                        '۷':'7','۸':'8','۹':'9'}

    result=""
    for char in string:
        try:
            char=persian2FinglishDic[char]
        except:
            pass
        result+=char
    return result

#chrome = Chrome(True)
#chrome.driver.get("https://www.codal.ir/ReportList.aspx?search&Symbol="+symbol+"&PageNumber="+str(pageNumber)+"&Audited&NotAudited&IsNotAudited=false&Childs=false&Mains&Publisher=false")
#assert "Codal" in chrome.driver.title
#ErrorPage = chrome.driver.find_element_by_class_name("text-danger")
#inf = chrome.driver.find_element_by_class_name("letter-title")
#inf.text) & (where('href') == inf.get_attribute("href"))):
#del chrome
class Chrome:
    driver=None
    counter=0
    def __init__(self, showUI):
        Chrome.counter+=1
        print(Chrome.counter)
        if not (Chrome.driver):
            options = webdriver.ChromeOptions()
            if not (showUI):
                options.add_argument('headless')
                options.add_argument('window-size=1920x1080')
                options.add_argument("disable-gpu")
            options.add_argument("--log-level=3");
            chromeWebDriverPath = 'D:/Desktop/بورس/04-pyton/chromedriver_win32/chromedriver.exe'
            Chrome.driver = webdriver.Chrome(executable_path=chromeWebDriverPath, options=options)
    def __del__(self):
        Chrome.counter-=1
        if (Chrome.counter<=1):
            Chrome.driver.close()
            
    def loadURLByTrackingNoOffline(self, symbol, url, tracingNo, value):
        filename = FilenameManager.get({'enum':FilenameManager.CatchHTML,'symbol':symbol,'tracingNo':tracingNo, 'value':value})
        try:
            f = open(filename, mode="r", encoding="utf-8")
            data = f.read()
            f.close()
            return data
        except Exception as err:
            try:
                Chrome.driver.get(url)
                pageSource = Chrome.driver.page_source
                #Todo: usevirtual filesystem
                #from fs.osfs import OSFS
                f = open(filename, "wb")
                s=pageSource.encode('UTF-8')
                f.write(s)
                f.close()
                return pageSource
            except Exception as err:
                print("Error in loading URL:"+filename)
                print(f'Other error occurred: {err}') 
#x = Chrome(True)
##y = Chrome(True)
##z = Chrome(True)
##import time;
#x.loadURLByTrackingNoOffline("http://google.com", "1","2")
#del x
##del y


class GroupProcess:
    def getSymbols(start, end, JustValidSymbols, callback):
        groupDB = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
        symbolsTable = groupDB.table('Symbols')
        symbols = symbolsTable.all()
        symbolsCounter = len(symbols)
        symbolIndex=0
        for symbol in symbols:
            symbolIndex+=1
            if (start):
                if (symbolIndex<int(start)):
                    continue
            if (end):
                if (symbolIndex>int(end)):
                    continue
            if not(JustValidSymbols):
                if (symbol['GroupName']=='Unknown' or symbol['st']==2 or symbol['st']==3):
                    continue
            callback(symbol, symbolIndex, symbolsCounter)
        groupDB.close()
   
    def getAllSymbols(self):
        groupDB = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
        symbolsTable = groupDB.table('Symbols')
        symbols = symbolsTable.all()
        groupDB.close()
##del z

class Timer:
    def __init__(self):
        self.start=datetime.now()
    def __del__(self):
        pass
    def watch(self):
        return datetime.now()-self.start
    def printWatch(self):
        print("                 Time:"+str(self.watch()))

