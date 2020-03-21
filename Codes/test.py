import requests
import requests
from bs4 import BeautifulSoup
import requests.packages.urllib3
import jsons
import time

from selenium import webdriver
import atexit

import threading
import datetime
import time

from tinydb import TinyDB, Query
from tinydb import where
from selenium.webdriver.common.keys import Keys

import sys

    
# chromeProfilePath='DB/General/ChromepProfile/'
chromeProfilePath='D:/Programming/Project/FATS/DB/General/ChromepProfile'
refreshUrl='https://onlineplus.mofidonline.com/Home/Default/page-1'
refreshMinutes=10
# cookieFile = 'DB/MofidOnlineCookieFile.json'
cookieFile = 'D:/Programming/Project/FATS/DB/MofidOnlineCookieFile.json'
# orderFile = 'DB/MofidOnlineOrderFile.json'
orderFile = 'D:/Programming/Project/FATS/DB/MofidTraderAutoSendOrder.json'
showUI = True
def doOperationAt_Time(doOperation, params, comment\
    , hourTarget, minuteTarget, secondTarget, microSecondTarget\
    , hourOffset, minuteOffset, secondOffset, microSecondOffset):
    
    hourTarget-=hourOffset
    minuteTarget-=minuteOffset
    secondTarget-=secondOffset
    microSecondTarget-=microSecondOffset
    

    def RealTimeTimerTriggerWorker():
        timeNow = datetime.datetime.now()
        secondsTarget=secondTarget+60*(minuteTarget+60*hourTarget)+microSecondTarget
        while(True):
            timeNow = datetime.datetime.now()
            seconds=timeNow.second+60*(timeNow.minute+60*timeNow.hour)+(0.000001*timeNow.microsecond)
            if (seconds>=secondsTarget):
                break
            time.sleep(0)
        print(seconds-secondsTarget)   
        timeNow = datetime.datetime.now()
        if (doOperation):
            if (params!=None):
                doOperation(params)
            else:
                doOperation() 
        print(timeNow, ':', comment)
        
    def secondTimeTimerTriggerWorker():
        secondsTarget=secondTarget+60*(minuteTarget+60*hourTarget)
        while(True):
            timeNow = datetime.datetime.now()
            seconds=timeNow.second+60*(timeNow.minute+60*timeNow.hour)
            if (seconds<secondsTarget):
                if(seconds+10>secondsTarget):
                    break
            time.sleep(1)
        RealTimeTimerThread = threading.Thread(target=RealTimeTimerTriggerWorker)
        RealTimeTimerThread.start()
        
    SecondTimeTimerThread = threading.Thread(target=secondTimeTimerTriggerWorker)
    SecondTimeTimerThread.start()

def loadChromeAndWaitToLoad():
    def checkIsLogin():
        #<a class="signout " href="/Account/Logout">
        inputStr="//a[@class='signout ' and @href='/Account/Logout']"
        signOutElems = driver.find_elements_by_xpath(inputStr) 
        if (signOutElems):
            return True
        return False
    
    def onClose():
        if (driver):
            driver.close()
        
    options = webdriver.ChromeOptions()
    if not (showUI):
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
    options.add_argument("--log-level=3");
    options.add_argument("user-data-dir="+chromeProfilePath) #Path to your chrome profile
    chromeWebDriverPath = 'D:/Desktop/بورس/04-pyton/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromeWebDriverPath, options=options)
    atexit.register(onClose)
    driver.get(refreshUrl)
    while(True):
        if (checkIsLogin()):break
        time.sleep(1)
    
    def autoRefreshChrome():
        def saveCookie2File():
            cookies=driver.get_cookies()
            try:
                db = TinyDB(cookieFile)
                db.purge_tables()
                db.insert_multiple(cookies)
                db.close()
            except Exception as err:
                print(f'Error in save cookie File: {err}') 
        def refresh():
            #driver.find_element_by_class_name('signout ').sendKeys(Keys.F5)
            driver.refresh()
        if not (checkIsLogin()):
            print("Error in Login!!")
            return
        saveCookie2File()
        refresh()
        targetTime = datetime.datetime.now() + datetime.timedelta(minutes=refreshMinutes)
        doOperationAt_Time(autoRefreshChrome, None, "Chrome refresh Triggered", \
            targetTime.hour, targetTime.minute, targetTime.second, 0.0,\
                0,0,0,0)
    
    autoRefreshChrome()


def loadAllsendBuyRequest():
    def sendBuyRequestNow(orderData):
        def loadCookieFromFile():
            db = TinyDB(cookieFile)
            cookiesDB = db.all()
            cookies={}
            for cookieDB in cookiesDB:
                cookies[cookieDB["name"]]=cookieDB["value"]
            db.close()
            return cookies
        
        requests.packages.urllib3.disable_warnings()
        try:
            sendOrderurl="https://onlineplus.mofidonline.com/Customer/SendOrder"
            
            postData={\
                "IsSymbolCautionAgreement":"false"
                ,"CautionAgreementSelected":"false"
                ,"IsSymbolSepahAgreement":"false"
                ,"SepahAgreementSelected":"false"
                ,"orderCount":orderData["orderCount"]
                ,"orderPrice":orderData["orderPrice"]
                ,"FinancialProviderId":"1"
                ,"minimumQuantity":""
                ,"maxShow":"0"
                ,"orderId":"0"
                ,"isin":orderData["isin"]
                ,"orderSide":"65"
                ,"orderValidity":"74"
                ,"orderValiditydate":"null"
                ,"shortSellIsEnabled":"false"
                ,"shortSellIncentivePercent":"0"
            }
            
            headers = {\
                # ":method":"POST"\
                # ,":scheme":"https"\
                # ,":authority":"onlineplus.mofidonline.com"\
                # ,":path":"/Customer/SendOrder"\
                #,"content-length":"371"\
                "sec-fetch-dest":"empty"\
                ,"x-requested-with":"XMLHttpRequest"\
                ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'\
                ,"content-type":"application/json"\
                ,"accept":"*/*"\
                ,"origin":"https://onlineplus.mofidonline.com"\
                ,"sec-fetch-site":"same-origin"\
                ,"sec-fetch-mode":"cors"\
                ,"referer":"https://onlineplus.mofidonline.com/Home/Default/page-1"\
                ,"accept-encoding":"gzip, deflate, br"\
                ,"accept-language":"en-US,en;q=0.9"\
                
                #,"cookie":
                ## lastmessage-6=1
                ## lastmessage-2=1060528
                ## lastmessage-4=1
                ## "UserHasReadedHelp=true; 
                # _ga=GA1.2.816572881.1569671965;
                #  GuidedTourVersion=1; 
                # SiteVersion=3.7.4; 
                # _gid=GA1.2.252721106.1584126160; 
                ## _AuthCookie={\"t\":\"\",\"p\":1}; 
                # silverse=105h0lilzyxndpiigtkdvj3f; 
                # crisp-client%2Fsession%2Fe95056ad-2681-452d-976d-0c2a304165c9=session_bb27ba3c-c5ad-41aa-a983-e6b1cf022809; 
                ## ASP.NET_SessionId=ru0y0x5yfcht1gnotz1keng1;
                # .ASPXAUTH=A01484135FB8B5662BFD98E7E64EAAEEA18BF3BB08E9C43D7E1D9044A547705A483920EB562FA06DB6885AB016B6CC800492CDC1974BE30AE04BCEBE639F7D3061AE0842E5F1FC558D8B275918F085A210B21C4B1541BFA5997C60080F89107DA00A171B8BADBB29063BAE6A9326CAAFC98C4376375FF02987EEBCD653EA55C7; 
                # Token=4f6d168e-62df-46aa-991b-a84f912140e8"
            }
            cookies = loadCookieFromFile()
            def requestWorker():
                response = requests.post(sendOrderurl\
                    , data=jsons.dumps(postData), headers=headers, cookies=cookies\
                    , verify = False, timeout=(10, 20))
                print(orderData)
                print(response.content)
                print(response.elapsed.total_seconds())
            threading.Thread(target=requestWorker).start()
                    
        except Exception as err:
            print(f'Other error occurred: {err}') 
            ErrorJson=True
    
    orderFileDB = TinyDB(orderFile)
    orderFileDatas = orderFileDB.all()
    for orderData in orderFileDatas:
        if (orderData["status"].strip().lower()=="done"):
            continue
        # orderCount=orderData["orderCount"]
        # orderPrice=orderData["orderPrice"]
		# isin=orderData["isin"]
		# isinName=orderData["isinName"]
        absoluteTime=orderData["absoluteTime"].split(":")
        hour=int(absoluteTime[0])
        minute=int(absoluteTime[1])
        second=int(absoluteTime[2])
        microSecond=int(absoluteTime[3])*0.000001
        doOperationAt_Time(sendBuyRequestNow, orderData, orderData["comment"]\
            , hour, minute, second, microSecond\
            , 0, 0, 0, 0.0)
        repeatTime=float(orderData["repeatTime"])
        repeatCount=int(orderData["repeatCount"])
        for counter in range(1,repeatCount):
            target=second+60*(minute+60*hour)+microSecond+(repeatTime*counter)
            microSecondTarget=target-int(target)
            target=int(target)
            secondTarget=target%60
            target=int(target/60)
            minuteTarget=target%60
            target=int(target/60)
            hourTarget=target
            if (target<24):
                doOperationAt_Time(sendBuyRequestNow, orderData, orderData["comment"]\
                , hourTarget, minuteTarget, secondTarget, microSecondTarget\
                , 0, 0, 0, 0.0)
    orderFileDB.close()
    
   
           
if __name__ == "__main__":
    if(len(sys.argv)>1):
        if (sys.argv[1].strip().lower()=="master"):
            loadChromeAndWaitToLoad()
        if (sys.argv[1].strip().lower()=="slave"):
            loadAllsendBuyRequest()
    else:    
        loadAllsendBuyRequest()
    
    #TODO 13990102:Do timig operation for log
    #TODO 13990102:best timer algorithm
    #TODO 13990102:Mirtual exclution with cookieFile
    #TODO 13990102:CreateUI For operation in order file
