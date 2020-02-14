from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3
import jsons
import time
from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import urllib.request
from selenium.webdriver.common.keys import Keys

class EasyTraderScraperClass:
    chrome=None
    
    def __init__(self):
        pass
    
    def openChrome(self):
        self.chrome = Chrome(True)
        
    def openEasyTraderInChrome(self):   
        url="https://account.emofid.com/Login"
        Chrome.driver.get(url)
        self.pageSource = Chrome.driver.page_source
    
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
        elem = Chrome.driver.find_element_by_name("Username")
        elem.clear()
        elem.send_keys(username)
        elem = Chrome.driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        url="https://d.easytrader.emofid.com"
        Chrome.driver.get(url)

    def saveCookieToDB(self):
        pass
        chromeCookies = Chrome.driver.get_cookies()
        chromeDB = TinyDB(FilenameManager.get({'enum':FilenameManager.ChromeData}))
        cookiesTable = chromeDB.table("Cookies")
        cookiesTable.insert_multiple(chromeCookies)
        chromeDB.close()
        

    def loadCookieFromDB(self):
        chromeCookies = Chrome.driver.get_cookies()
        chromeDB = TinyDB(FilenameManager.get({'enum':FilenameManager.ChromeData}))
        cookiesTable = chromeDB.table("Cookies")
        cookies=cookiesTable.all()
        chromeDB.close()
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
        del self.chrome