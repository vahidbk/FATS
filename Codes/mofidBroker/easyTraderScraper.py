from bs4 import BeautifulSoup
import jsons
import time
from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import urllib.request
from requestium import Session, Keys

class EasyTraderScraperClass:
    session=None
    
    def __init__(self):
        pass
    
    def openChrome(self):
        options = {'--log-level':'3', 'user-data-dir':FilenameManager.get({'enum':FilenameManager.ChromeProfile})}
        self.session = Session(webdriver_path='D:/Desktop/بورس/04-pyton/chromedriver_win32/chromedriver.exe', \
            browser='chrome',\
            default_timeout=15,\
            webdriver_options=options)
        
    def openEasyTraderInChrome(self):   
        url="https://account.emofid.com/Login"
        #self.session.transfer_session_cookies_to_driver()
        self.session.driver.get(url)
        self.pageSource = self.session.driver.page_source
    
    def loginEasyTrader(self):
        mofidEasyTrader = "MofidEasyTrader"
        try:
            db = TinyDB(FilenameManager.get({'enum':FilenameManager.LoginData}))
            userTable = db.table(mofidEasyTrader)
            user = userTable.all()
            username=user[0]["Username"]
            password=user[0]["Password"]
            db.close()
        except:
            print("Error in username and password Easy Trader.")
            db.purge_table(mofidEasyTrader)
            userTable = db.table(mofidEasyTrader)
            userTable.insert({"Username":"TypeUserNameHere", "Password":"typePasswordHere"})
            db.close()
        try:
            soup = BeautifulSoup(self.pageSource,"lxml")
            #<input name="__RequestVerificationToken" type="hidden" value="CfDJ8AHl50NrxGlBhHIn7WEJdiXL3owMe4qGfUZAQVG-5a425BzA1lJLUAaf619xqOgGxgxKKKDpGvsnzUdNWC_wNbE2-2oANcZbsiITpEMJF9gRu9pS2HlacTFLTBzoei80_rUKLOcPJsJYOfA2pIKL8C0">
            requestVerificationTokenInput = soup.find('input', attrs={'name':'__RequestVerificationToken'})
            requestVerificationToken = requestVerificationTokenInput.attrs['value']
        except Exception as err:
            print(f'Error Comment: {err}')
        elem = self.session.driver.find_element_by_name("Username")
        elem.clear()
        elem.send_keys(username)
        elem = self.session.driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        url="https://d.easytrader.emofid.com"
        self.session.driver.get(url)

    def saveCookieToDB(self):
        url="https://d.easytrader.emofid.com"
        self.session.driver.get(url)

    def loadCookieFromDB(self):
        self.session.transfer_driver_cookies_to_session()
        #self.session.post('http://www.google.com/', data={'key1': 'value1'}) 
        #self.sessions.get('http://www.google.com/') 
        #self.session.options('http://www.google.com/') 


        url='https://d11.emofid.com/easy/api/Money/GetRemain'
        response1 = self.session.options(url, verify = False)
        response2 = self.session.get(url,verify = False)
        # {"realBalance":5523736.0,"blockedBalance":0.0,"accountBalance":5523736.0}
        #x=1
        pass
        
    def testResponce(self):
        pass
        theSubjectsTableData = theSubjectsTable.all()
        requestSession = requests.Session()
        for cookie in chromeCookies:
            requestSession.cookies.set(cookie['name'], cookie['value'])
        requests.packages.urllib3.disable_warnings()
        # response = requests.post(url \
        #     }, verify = False, timeout=(10, 20))
    def closeChrome(self):
        self.session.chrome.close()