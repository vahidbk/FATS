from bs4 import BeautifulSoup
import jsons
import time
from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import urllib.request
from requestium import Session, Keys

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


    def loadEasyTrader(self):
        url="https://d.easytrader.emofid.com"
        Chrome.driver.get(url) 

    def openSearchMenu(self):
        elems = Chrome.driver.find_elements_by_class_name("menu_item_panel")
        searchMenu=None
        searchString="جستجو"
        # for elem in elems:
        #     if elem.get_text(strip=True).replace("\n", "").find(searchString)>-1:
        #         searchMenu=elem
        searchMenu=elems[0]
        searchMenu.click()
    
    def closeSearchMenu(self):
        Chrome.driver.send_keys(Keys.ESCAPE).perform()
    
    #todo:test it    
    def focusOnSymbol(self):
        if not openSearchMenu(self): return False
        
        elem.click()
        
        inputStr="//input[@placeholder='نماد مورد جستجو را وارد کنید']"
        elem = Chrome.driver.find_element_by_xpath(inputStr)
        symbol="کویر"
        elem.send_keys(symbol)
        Chrome.driver.implicitly_wait(1) 
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.RETURN)
        
        if (elem == Chrome.driver.find_element_by_xpath(inputStr)):
            closeSearchMenu()
            return False    
        return True
    
    def getCurrentFocusedSymbol():
        elem = Chrome.driver.findElement(By.xpath("//h5[@class='mb-0 text-truncate']"));
        return elem.get_text(strip=True).replace("\n", "")
    
    def getCurrentFocusedSymbolFullname():
        elem = Chrome.driver.findElement(By.xpath("//h5[@class='mb-0 text-truncate']"));
        next_sibling = Chrome.driver.execute_script("""return arguments[0].nextElementSibling""", elem)
        return next_sibling
    
    def lastCostSymbol():
        pass
    
    def rangeCostSymbol():
        pass
    
    def firstPriceSymbol():
        pass
    
    def sellQueueSymbol():
        pass
    
    def buyQueueSymbol():
        pass
    
    def buyAndSellPercentMaxDifSymbol():
        pass
    
    def buyAndSellPercentCurrentDifSymbol():
        pass
    
    def haghigiHoghogiDataSymbol():
        pass
    
    def efficiencyDaySymbol():
        pass
    
    def efficiencyWeekSymbol():
        pass    
    
    def efficiencyMonthSymbol():
        pass    
    
    def startBuySymbol():
        elem = Chrome.driver.findElement(By.xpath("//button[@class='btn btn-sm btn-outline-success btn-block ml-1']"));
        elem.click()

    def startSellSymbol():
        elem = Chrome.driver.findElement(By.xpath("//button[@class='btn btn-sm btn-outline-danger btn-block mt-0 mr-1']"));
        elem.click()
    
    def initializeBuySymbol():
        
        pass

    def initializeSellSymbol():
        pass
    
    def fillBuySellForm():
        pass
    
    def DoneBuySellOperationNow():
        pass
    

    def saveCookieToDB(self):
        pass

    def loadCookieFromDB(self):
        pass
        
    def testResponce(self):
        pass

    def closeChrome(self):
        del self.chrome