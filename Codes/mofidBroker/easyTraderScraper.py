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

    def openSearchMenu(self): #internal
        elems = Chrome.driver.find_elements_by_class_name("menu_item_panel")
        searchMenu=None
        searchString="جستجو"
        # for elem in elems:
        #     if elem.get_text(strip=True).replace("\n", "").find(searchString)>-1:
        #         searchMenu=elem
        searchMenu=elems[0]
        return searchMenu
    
    def closeSearchMenu(self): #internal
        Chrome.driver.send_keys(Keys.ESCAPE)
    
    #todo:test it    
    def focusOnSymbol(self):
        elem=self.openSearchMenu()
        if not elem: 
            return False
        
        elem.click()
        
        inputStr="//input[@placeholder='نماد مورد جستجو را وارد کنید']"
        elem = Chrome.driver.find_element_by_xpath(inputStr)
        symbol="سشرق"
        elem.send_keys(symbol)
        Chrome.driver.implicitly_wait(1) 
        time.sleep(1)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.RETURN)
        
        try:
            Chrome.driver.find_element_by_xpath(inputStr)
            print(f'Error : Not focus on symbol') 
            self.closeSearchMenu()
            return False 
        except Exception as err:
            pass  
        
        return True
    
    def startBuySymbol(self):
        inputStr="//button[@class='btn btn-sm btn-outline-success btn-block ml-1']"
        elems = Chrome.driver.find_elements_by_xpath(inputStr)
        elems[0].click()

    #todo:test it
    def startSellSymbol(self):
        inputStr="//button[@class='btn btn-sm btn-outline-danger btn-block mt-0 mr-1']"
        elems = Chrome.driver.find_elements_by_xpath(inputStr)
        elems[0].click()
    
    #todo:test it    
    def getCurrentFocusedSymbol(self):
        elem = Chrome.driver.find_elements_by_xpath("//h5[@class='mb-0 text-truncate']")
        return elem[0].get_text(strip=True).replace("\n", "")
    
    #todo:test it
    def getCurrentFocusedSymbolFullname(self):
        elems = Chrome.driver.find_elements_by_xpath("//h5[@class='mb-0 text-truncate']")
        next_sibling = Chrome.driver.execute_script("""return arguments[0].nextElementSibling""", elems[0])
        return next_sibling
    
    #todo:test it
    def getcurrentStatusOfBuyAndSellMenuStock(self):
        inputStr="//div[@class='stocks flex-fill overflow-auto h-100']"
        root = Chrome.driver.find_elements_by_xpath(inputStr)[0]
        inputStr="//div[@class='stock shadow-sm user-select-none buy']"
        titleItem = Chrome.driver.find_elements_by_xpath(inputStr)[0]
        # BuySellMenuStatusStock
        # <div _ngcontent-fuj-c20="" class="stocks flex-fill overflow-auto h-100"><!----><!----><!----><div _ngcontent-fuj-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-fuj-c20="" d-order-list-item="" _nghost-fuj-c31=""><div _ngcontent-fuj-c31="" class="stock shadow-sm user-select-none buy" title="در حال ارسال به هسته معاملات"><div _ngcontent-fuj-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-fuj-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-fuj-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-fuj-c31="" class="mb-0">گویان</h6></div><div _ngcontent-fuj-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-fuj-c31="" class="mdi mdi-20px line-height-none mdi-check text-secondary"></span><div _ngcontent-fuj-c31="" class="stock-actions"><!----><!----><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-pencil-outline text-muted" title="ویرایش"></span><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted" title="حذف"></span></div></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between"><span _ngcontent-fuj-c31="">3,000</span><span _ngcontent-fuj-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-fuj-c31="" class="progress my-1"><div _ngcontent-fuj-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 0%;"></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-fuj-c31="" class="order-price">4,380 ریال</span><span _ngcontent-fuj-c31=""><small _ngcontent-fuj-c31="" class="order-date text-muted">10:10:12 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div><div _ngcontent-fuj-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-fuj-c20="" d-order-list-item="" _nghost-fuj-c31=""><div _ngcontent-fuj-c31="" class="stock shadow-sm user-select-none buy done" title="انجام شده"><div _ngcontent-fuj-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-fuj-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-fuj-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-fuj-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-fuj-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-fuj-c31="" class="mdi mdi-20px line-height-none mdi-check-all text-primary"></span><div _ngcontent-fuj-c31="" class="stock-actions"><!----><!----><!----><!----></div></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between"><span _ngcontent-fuj-c31="">1,000</span><span _ngcontent-fuj-c31="" class="text-start"> ( 100% ) 1,000 </span></div><div _ngcontent-fuj-c31="" class="progress my-1"><div _ngcontent-fuj-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 100%;"></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-fuj-c31="" class="order-price">7,065 ریال</span><span _ngcontent-fuj-c31=""><small _ngcontent-fuj-c31="" class="order-date text-muted">08:42:08 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div><div _ngcontent-fuj-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-fuj-c20="" d-order-list-item="" _nghost-fuj-c31=""><div _ngcontent-fuj-c31="" class="stock shadow-sm user-select-none buy done" title="انجام شده"><div _ngcontent-fuj-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-fuj-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-fuj-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-fuj-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-fuj-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-fuj-c31="" class="mdi mdi-20px line-height-none mdi-check-all text-primary"></span><div _ngcontent-fuj-c31="" class="stock-actions"><!----><!----><!----><!----></div></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between"><span _ngcontent-fuj-c31="">500</span><span _ngcontent-fuj-c31="" class="text-start"> ( 100% ) 500 </span></div><div _ngcontent-fuj-c31="" class="progress my-1"><div _ngcontent-fuj-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 100%;"></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-fuj-c31="" class="order-price">7,065 ریال</span><span _ngcontent-fuj-c31=""><small _ngcontent-fuj-c31="" class="order-date text-muted">08:30:07 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div><div _ngcontent-fuj-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-fuj-c20="" d-order-list-item="" _nghost-fuj-c31=""><div _ngcontent-fuj-c31="" class="stock shadow-sm user-select-none buy" title="در حال ارسال به هسته معاملات"><div _ngcontent-fuj-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-fuj-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-fuj-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-fuj-c31="" class="mb-0">گویان</h6></div><div _ngcontent-fuj-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-fuj-c31="" class="mdi mdi-20px line-height-none mdi-check text-secondary"></span><div _ngcontent-fuj-c31="" class="stock-actions"><!----><!----><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-pencil-outline text-muted" title="ویرایش"></span><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted" title="حذف"></span></div></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between"><span _ngcontent-fuj-c31="">100</span><span _ngcontent-fuj-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-fuj-c31="" class="progress my-1"><div _ngcontent-fuj-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 0%;"></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-fuj-c31="" class="order-price">4,380 ریال</span><span _ngcontent-fuj-c31=""><small _ngcontent-fuj-c31="" class="order-date text-muted">10:01:25 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div></div>
        # دخواست خرید
        #<div _ngcontent-oqj-c20=""><order-form _ngcontent-oqj-c20="" _nghost-oqj-c30=""><!----><!----><div _ngcontent-oqj-c30="" class="stock shadow-sm mb-2 user-select-none overflow-hidden buy"><div _ngcontent-oqj-c30="" class="p-2 position-relative"><div _ngcontent-oqj-c30="" class="mb-2 order-stock-symbol d-flex justify-content-between align-items-center"><div _ngcontent-oqj-c30="" class="h6 mb-0 d-flex"> سشرق </div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center"><div _ngcontent-oqj-c30="" class="text-right order-side d-flex align-items-center order-side--buy"><span _ngcontent-oqj-c30="" class="ml-1 text-success"> خرید</span><div _ngcontent-oqj-c30="" class="custom-control custom-switch"><input _ngcontent-oqj-c30="" class="custom-control-input" id="customSwitch1" type="checkbox"><label _ngcontent-oqj-c30="" class="custom-control-label" for="customSwitch1"></label></div></div><!----><span _ngcontent-oqj-c30="" class="mdi mdi-18px px-1 rounded mdi-close text-grey"></span></div></div><!----><!----><form _ngcontent-oqj-c30="" novalidate="" class="ng-pristine ng-valid ng-touched"><div _ngcontent-oqj-c30=""><div _ngcontent-oqj-c30="" class="order-form-field"><div _ngcontent-oqj-c30="" class="d-flex form-control p-0 h-auto position-relative"><small _ngcontent-oqj-c30="" class="text-reverse-50 position-absolute" style="pointer-events: none; top: 2px; right:4px">تعداد</small><dx-number-box _ngcontent-oqj-c30="" class="d-flex align-items-center px-1 bg-principal ng-pristine ng-valid dx-show-invalid-badge dx-numberbox dx-texteditor dx-editor-outlined dx-widget ng-touched" dir="ltr" formcontrolname="quantity" format="#,##0" id="quantity" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><input type="hidden" value="10000"><div class="dx-texteditor-container"><div class="dx-texteditor-input-container"><input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="1" max="undefined" step="10000" aria-valuemin="1" aria-valuemax="" aria-valuenow="10000" role="spinbutton"><div data-dx_placeholder="" class="dx-placeholder dx-state-invisible"></div></div><div class="dx-texteditor-buttons-container"><div></div><div></div></div></div></dx-number-box><div _ngcontent-oqj-c30="" class="d-flex flex-column medium border-left border-right" style="min-width: 80px; min-height: 45px;"><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 border-bottom cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-up line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">100,000</span></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-down line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">1</span></div></div><span _ngcontent-oqj-c30="" class="mdi mdi-20px mdi-calculator d-flex justify-content-center align-items-center px-2 cup text-muted"></span></div></div><!----><div _ngcontent-oqj-c30="" class="order-form-field mt-1"><div _ngcontent-oqj-c30="" class="d-flex form-control p-0 h-auto position-relative"><small _ngcontent-oqj-c30="" class="text-reverse-50 position-absolute" style="pointer-events: none; top: 2px; right:4px">قیمت</small><dx-number-box _ngcontent-oqj-c30="" class="d-flex align-items-center px-1 bg-principal ng-untouched ng-pristine dx-show-invalid-badge dx-numberbox dx-texteditor dx-editor-outlined dx-widget ng-valid" dir="ltr" formcontrolname="price" format="#,##0" id="price" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><input type="hidden" value="7065"><div class="dx-texteditor-container"><div class="dx-texteditor-input-container"><input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="undefined" max="undefined" step="35" aria-valuemin="" aria-valuemax="" aria-valuenow="7065" role="spinbutton"><div data-dx_placeholder="" class="dx-placeholder dx-state-invisible"></div></div><div class="dx-texteditor-buttons-container"><div></div><div></div></div></div></dx-number-box><div _ngcontent-oqj-c30="" class="d-flex flex-column medium border-left border-right" style="min-width: 80px; min-height: 45px;"><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 border-bottom cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-up line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">7,065</span></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-down line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">6,393</span></div></div><span _ngcontent-oqj-c30="" class="mdi mdi-20px d-flex justify-content-center align-items-center px-2 cup text-muted mdi-lock-open-outline"></span></div></div></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-end align-items-center"><div _ngcontent-oqj-c30="" class="custom-control custom-checkbox my-1"><label _ngcontent-oqj-c30="" class="ml-1 mb-0" for="customCheck1سشرق">پیشرفته</label><input _ngcontent-oqj-c30="" class="custom-control-input" type="checkbox" id="customCheck1سشرق"><label _ngcontent-oqj-c30="" class="custom-control-label" for="customCheck1سشرق"></label></div></div><!----><div _ngcontent-oqj-c30="" class="d-flex"><button _ngcontent-oqj-c30="" class="col-7 btn btn-sm btn-success flex-grow-1 px-0" title="(Enter)" type="submit"><!----><span _ngcontent-oqj-c30="">ارسال خرید</span><!----></button><button _ngcontent-oqj-c30="" class="col btn btn-sm mr-1 px-0 btn-outline-warning" title="(Esc)" type="button">پیش&zwnj;نویس</button></div><div _ngcontent-oqj-c30="" class="mt-2 medium"><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">دارایی فعلی : </span><span _ngcontent-oqj-c30="" class="col-6 text-start cup" dir="ltr">0</span></div><!----><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">قیمت سر&zwnj;به&zwnj;سر: </span><span _ngcontent-oqj-c30="" class="col-6 text-start" dir="ltr">7,167</span></div><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">هزینه معامله: </span><span _ngcontent-oqj-c30="" class="col-6 text-start" dir="ltr">327,816</span></div><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">جمع کل:</span><span _ngcontent-oqj-c30="" class="col-6 text-start" dir="ltr">70,977,816</span></div></div></form></div></div><!----></order-form></div>
        # درخواست فروش
        #<div _ngcontent-oqj-c20=""><order-form _ngcontent-oqj-c20="" _nghost-oqj-c30=""><!----><!----><div _ngcontent-oqj-c30="" class="stock shadow-sm mb-2 user-select-none overflow-hidden sell"><div _ngcontent-oqj-c30="" class="p-2 position-relative"><div _ngcontent-oqj-c30="" class="mb-2 order-stock-symbol d-flex justify-content-between align-items-center"><div _ngcontent-oqj-c30="" class="h6 mb-0 d-flex"> سشرق </div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center"><div _ngcontent-oqj-c30="" class="text-right order-side d-flex align-items-center order-side--sell"><span _ngcontent-oqj-c30="" class="ml-1 text-danger"> فروش</span><div _ngcontent-oqj-c30="" class="custom-control custom-switch"><input _ngcontent-oqj-c30="" class="custom-control-input" id="customSwitch1" type="checkbox"><label _ngcontent-oqj-c30="" class="custom-control-label" for="customSwitch1"></label></div></div><!----><span _ngcontent-oqj-c30="" class="mdi mdi-18px px-1 rounded mdi-close text-grey"></span></div></div><!----><!----><form _ngcontent-oqj-c30="" novalidate="" class="ng-pristine ng-valid ng-touched"><div _ngcontent-oqj-c30=""><div _ngcontent-oqj-c30="" class="order-form-field"><div _ngcontent-oqj-c30="" class="d-flex form-control p-0 h-auto position-relative"><small _ngcontent-oqj-c30="" class="text-reverse-50 position-absolute" style="pointer-events: none; top: 2px; right:4px">تعداد</small><dx-number-box _ngcontent-oqj-c30="" class="d-flex align-items-center px-1 bg-principal ng-pristine ng-valid dx-show-invalid-badge dx-numberbox dx-texteditor dx-editor-outlined dx-widget ng-touched" dir="ltr" formcontrolname="quantity" format="#,##0" id="quantity" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><input type="hidden" value="5000"><div class="dx-texteditor-container"><div class="dx-texteditor-input-container"><input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="1" max="undefined" step="5000" aria-valuemin="1" aria-valuemax="" aria-valuenow="5000" role="spinbutton"><div data-dx_placeholder="" class="dx-placeholder dx-state-invisible"></div></div><div class="dx-texteditor-buttons-container"><div></div><div></div></div></div></dx-number-box><div _ngcontent-oqj-c30="" class="d-flex flex-column medium border-left border-right" style="min-width: 80px; min-height: 45px;"><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 border-bottom cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-up line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">100,000</span></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-down line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">1</span></div></div><span _ngcontent-oqj-c30="" class="mdi mdi-20px mdi-calculator d-flex justify-content-center align-items-center px-2 cup text-muted"></span></div></div><!----><div _ngcontent-oqj-c30="" class="order-form-field mt-1"><div _ngcontent-oqj-c30="" class="d-flex form-control p-0 h-auto position-relative"><small _ngcontent-oqj-c30="" class="text-reverse-50 position-absolute" style="pointer-events: none; top: 2px; right:4px">قیمت</small><dx-number-box _ngcontent-oqj-c30="" class="d-flex align-items-center px-1 bg-principal ng-untouched ng-pristine dx-show-invalid-badge dx-numberbox dx-texteditor dx-editor-outlined dx-widget ng-valid" dir="ltr" formcontrolname="price" format="#,##0" id="price" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><input type="hidden" value="6729"><div class="dx-texteditor-container"><div class="dx-texteditor-input-container"><input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="undefined" max="undefined" step="34" aria-valuemin="" aria-valuemax="" aria-valuenow="6729" role="spinbutton"><div data-dx_placeholder="" class="dx-placeholder dx-state-invisible"></div></div><div class="dx-texteditor-buttons-container"><div></div><div></div></div></div></dx-number-box><div _ngcontent-oqj-c30="" class="d-flex flex-column medium border-left border-right" style="min-width: 80px; min-height: 45px;"><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 border-bottom cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-up line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">7,065</span></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-between align-items-center p-1_2 cup h-100"><span _ngcontent-oqj-c30="" class="mdi mdi-18px mdi-chevron-down line-height-none"></span><span _ngcontent-oqj-c30="" class="position-relative flex-grow-1 text-center" style="top:1px">6,393</span></div></div><span _ngcontent-oqj-c30="" class="mdi mdi-20px d-flex justify-content-center align-items-center px-2 cup text-muted mdi-lock-open-outline"></span></div></div></div><div _ngcontent-oqj-c30="" class="d-flex justify-content-end align-items-center"><div _ngcontent-oqj-c30="" class="custom-control custom-checkbox my-1"><label _ngcontent-oqj-c30="" class="ml-1 mb-0" for="customCheck1سشرق">پیشرفته</label><input _ngcontent-oqj-c30="" class="custom-control-input" type="checkbox" id="customCheck1سشرق"><label _ngcontent-oqj-c30="" class="custom-control-label" for="customCheck1سشرق"></label></div></div><!----><div _ngcontent-oqj-c30="" class="d-flex"><button _ngcontent-oqj-c30="" class="col-7 btn btn-sm flex-grow-1 px-0 btn-danger" title="(Enter)" type="submit"><!----><!----><span _ngcontent-oqj-c30="">ارسال فروش</span></button><button _ngcontent-oqj-c30="" class="col btn btn-sm mr-1 px-0 btn-outline-warning" title="(Esc)" type="button">پیش&zwnj;نویس</button></div><div _ngcontent-oqj-c30="" class="mt-2 medium"><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">دارایی فعلی : </span><span _ngcontent-oqj-c30="" class="col-6 text-start cup" dir="ltr">0</span></div><!----><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">هزینه معامله: </span><span _ngcontent-oqj-c30="" class="col-6 text-start" dir="ltr">328,039</span></div><div _ngcontent-oqj-c30="" class="row"><span _ngcontent-oqj-c30="" class="col-6 text-reverse-50">جمع کل:</span><span _ngcontent-oqj-c30="" class="col-6 text-start" dir="ltr">33,316,961</span></div></div></form></div></div><!----></order-form></div>
        # در حال ارسال به هسته معاملات
        #<div _ngcontent-fuj-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-fuj-c20="" d-order-list-item="" _nghost-fuj-c31=""><div _ngcontent-fuj-c31="" class="stock shadow-sm user-select-none buy" title="در حال ارسال به هسته معاملات"><div _ngcontent-fuj-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-fuj-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-fuj-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-fuj-c31="" class="mb-0">گویان</h6></div><div _ngcontent-fuj-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-fuj-c31="" class="mdi mdi-20px line-height-none mdi-check text-secondary"></span><div _ngcontent-fuj-c31="" class="stock-actions"><!----><!----><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-pencil-outline text-muted" title="ویرایش"></span><!----><span _ngcontent-fuj-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted" title="حذف"></span></div></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between"><span _ngcontent-fuj-c31="">3,000</span><span _ngcontent-fuj-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-fuj-c31="" class="progress my-1"><div _ngcontent-fuj-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 0%;"></div></div><div _ngcontent-fuj-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-fuj-c31="" class="order-price">4,380 ریال</span><span _ngcontent-fuj-c31=""><small _ngcontent-fuj-c31="" class="order-date text-muted">10:10:12 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div>
        # ثبت در هسته معاملات
        #<div _ngcontent-wpm-c20="" class="d-order-list-item mb-2 ng-star-inserted"><!----><div _ngcontent-wpm-c20="" d-order-list-item="" _nghost-wpm-c31="" class="ng-star-inserted"><div _ngcontent-wpm-c31="" class="stock shadow-sm user-select-none buy" title="ثبت در هسته معاملات"><div _ngcontent-wpm-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-wpm-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-wpm-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-wpm-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-wpm-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-wpm-c31="" class="mdi mdi-20px line-height-none mdi-check text-success"></span><div _ngcontent-wpm-c31="" class="stock-actions"><!----><!----><!----><span _ngcontent-wpm-c31="" class="icon mdi mdi-18px px-1 mdi-pencil-outline text-muted ng-star-inserted" title="ویرایش"></span><!----><span _ngcontent-wpm-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted ng-star-inserted" title="حذف"></span></div></div></div><div _ngcontent-wpm-c31="" class="d-flex justify-content-between"><span _ngcontent-wpm-c31="">500</span><span _ngcontent-wpm-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-wpm-c31="" class="progress my-1"><div _ngcontent-wpm-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar"></div></div><div _ngcontent-wpm-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-wpm-c31="" class="order-price">7,065 ریال</span><span _ngcontent-wpm-c31=""><small _ngcontent-wpm-c31="" class="order-date text-muted hasOrderPlace">08:29:36 1398/12/17</small><!----><small _ngcontent-wpm-c31="" class="icon mdi mdi-18px px-1 mdi-information-outline text-grey ng-star-inserted" title="جایگاه سفارش" triggers="manual"></small><!----><!----></span></div></div></div></div><!----><!----></div>
        # مانده کافی نمی باشد
        # <div _ngcontent-crv-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-crv-c20="" d-order-list-item="" _nghost-crv-c31=""><div _ngcontent-crv-c31="" class="stock shadow-sm user-select-none buy" title="مانده کافی نمی باشد"><div _ngcontent-crv-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-crv-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-crv-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-crv-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-crv-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-crv-c31="" class="mdi mdi-20px line-height-none mdi-alert text-warning"></span><div _ngcontent-crv-c31="" class="stock-actions"><!----><!----><!----><!----><span _ngcontent-crv-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted" title="حذف"></span></div></div></div><div _ngcontent-crv-c31="" class="d-flex justify-content-between"><span _ngcontent-crv-c31="">10,000</span><span _ngcontent-crv-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-crv-c31="" class="progress my-1"><div _ngcontent-crv-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar"></div></div><div _ngcontent-crv-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-crv-c31="" class="order-price">7,065 ریال</span><span _ngcontent-crv-c31=""><small _ngcontent-crv-c31="" class="order-date text-muted">08:42:51 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div>
        # در حال ارسال سفارش
        # <div _ngcontent-crv-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-crv-c20="" d-order-list-item="" _nghost-crv-c31=""><div _ngcontent-crv-c31="" class="stock shadow-sm user-select-none buy" title="در حال ارسال سفارش"><div _ngcontent-crv-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-crv-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-crv-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-crv-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-crv-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-crv-c31="" class="mdi mdi-20px line-height-none mdi-vanish mdi-spin text-secondary"></span><div _ngcontent-crv-c31="" class="stock-actions"><!----><!----><!----><!----></div></div></div><div _ngcontent-crv-c31="" class="d-flex justify-content-between"><span _ngcontent-crv-c31="">100,000</span><span _ngcontent-crv-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-crv-c31="" class="progress my-1"><div _ngcontent-crv-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar"></div></div><div _ngcontent-crv-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-crv-c31="" class="order-price">7,065 ریال</span><span _ngcontent-crv-c31=""><small _ngcontent-crv-c31="" class="order-date text-muted">08:46:19 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div>
        # خطا در ارسال سفارش
        # <div _ngcontent-wpm-c20="" class="d-order-list-item mb-2 ng-star-inserted"><!----><div _ngcontent-wpm-c20="" d-order-list-item="" _nghost-wpm-c31="" class="ng-star-inserted"><div _ngcontent-wpm-c31="" class="stock shadow-sm user-select-none buy" title="خطا در ارسال سفارش"><div _ngcontent-wpm-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-wpm-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-wpm-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-wpm-c31="" class="mb-0">شگویا</h6></div><div _ngcontent-wpm-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-wpm-c31="" class="mdi mdi-20px line-height-none mdi-alert text-warning"></span><div _ngcontent-wpm-c31="" class="stock-actions"><!----><!----><!----><!----><span _ngcontent-wpm-c31="" class="icon mdi mdi-18px px-1 mdi-trash-can-outline text-muted ng-star-inserted" title="حذف"></span></div></div></div><div _ngcontent-wpm-c31="" class="d-flex justify-content-between"><span _ngcontent-wpm-c31="">100</span><span _ngcontent-wpm-c31="" class="text-start"> ( 0% ) 0 </span></div><div _ngcontent-wpm-c31="" class="progress my-1"><div _ngcontent-wpm-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar"></div></div><div _ngcontent-wpm-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-wpm-c31="" class="order-price">4,380 ریال</span><span _ngcontent-wpm-c31=""><small _ngcontent-wpm-c31="" class="order-date text-muted"></small><!----><!----></span></div></div></div></div><!----><!----></div>
        # انجام شده
        # <div _ngcontent-ujl-c20="" class="d-order-list-item mb-2"><!----><div _ngcontent-ujl-c20="" d-order-list-item="" _nghost-ujl-c31=""><div _ngcontent-ujl-c31="" class="stock shadow-sm user-select-none buy done" title="انجام شده"><div _ngcontent-ujl-c31="" class="py-2 px-2 position-relative"><!----><div _ngcontent-ujl-c31="" class="order-stock-symbol d-flex justify-content-between align-items-center mb-2"><div _ngcontent-ujl-c31="" class="d-flex mb-0"><!----><h6 _ngcontent-ujl-c31="" class="mb-0">سشرق</h6></div><div _ngcontent-ujl-c31="" class="d-flex align-items-center pr-3"><span _ngcontent-ujl-c31="" class="mdi mdi-20px line-height-none mdi-check-all text-primary"></span><div _ngcontent-ujl-c31="" class="stock-actions"><!----><!----><!----><!----></div></div></div><div _ngcontent-ujl-c31="" class="d-flex justify-content-between"><span _ngcontent-ujl-c31="">1,000</span><span _ngcontent-ujl-c31="" class="text-start"> ( 100% ) 1,000 </span></div><div _ngcontent-ujl-c31="" class="progress my-1"><div _ngcontent-ujl-c31="" aria-valuemax="100" aria-valuemin="0" aria-valuenow="25" class="progress-bar" role="progressbar" style="width: 100%;"></div></div><div _ngcontent-ujl-c31="" class="d-flex justify-content-between align-items-center"><span _ngcontent-ujl-c31="" class="order-price">7,065 ریال</span><span _ngcontent-ujl-c31=""><small _ngcontent-ujl-c31="" class="order-date text-muted">08:42:08 1398/12/17</small><!----><!----></span></div></div></div></div><!----><!----></div>
     
    def initializeBuySymbol(self):
        ## مسیر رسیدن به پنجره
        ## <div _ngcontent-ojc-c20="" class="stocks flex-fill overflow-auto h-100">
        inputStr="//div[@class='stocks flex-fill overflow-auto h-100']"
        rootElem = Chrome.driver.find_elements_by_xpath(inputStr)[0]
        ## <order-form _ngcontent-ojc-c20="" _nghost-ojc-c30="">
        inputStr="//order-form"
        orderFormElem = rootElem.find_elements_by_xpath(inputStr)[0]
        ## <div _ngcontent-ojc-c30="" class="stock shadow-sm mb-2 user-select-none overflow-hidden buy">
        #inputStr="//div[@class='stock shadow-sm mb-2 user-select-none overflow-hidden buy']"
        #orderForm = root.find_elements_by_xpath(inputStr)[0]
        # <div _ngcontent-ojc-c30="" class="p-2 position-relative">
            #عنوان سهم، خرید یا فروش و بستن پنجره
            # <div _ngcontent-ojc-c30="" class="mb-2 order-stock-symbol d-flex justify-content-between align-items-center">
        inputStr="//div[@class='mb-2 order-stock-symbol d-flex justify-content-between align-items-center']"
        titleMenuElem = orderFormElem.find_elements_by_xpath(inputStr)[0]
                ##نام نماد
                ##<div _ngcontent-ojc-c30="" class="h6 mb-0 d-flex"> طلا </div>
        inputStr="//div[@class='h6 mb-0 d-flex']"
        titleMenuSymbolElem = titleMenuElem.find_elements_by_xpath(inputStr)[0]
        titleMenuSymbol=titleMenuSymbolElem.get_text(strip=True).replace("\n", "")
                ##خرید یا فروش بودن
                ##<div _ngcontent-ojc-c30="" class="text-right order-side d-flex align-items-center order-side--buy">
        inputStr="//div[@class='text-right order-side d-flex align-items-center order-side--buy']"
        buyElem = titleMenuElem.find_elements_by_xpath(inputStr)[0]                
                ##or
                ##<div _ngcontent-ojc-c30="" class="text-right order-side d-flex align-items-center order-side--sell">
        inputStr="//div[@class='text-right order-side d-flex align-items-center order-side--sell']"
        sellElem = titleMenuElem.find_elements_by_xpath(inputStr)[0]                 
                ##بستن پنجره
                ##<span _ngcontent-ojc-c30="" class="mdi mdi-18px px-1 rounded mdi-close text-grey"></span>
        inputStr="//span[@class='mdi mdi-18px px-1 rounded mdi-close text-grey']"
        closeIconElem = titleMenuElem.find_elements_by_xpath(inputStr)[0]                 
            # فرم تعداد و قیمت سهم            
            # <form _ngcontent-ojc-c30="" novalidate="" class="ng-pristine ng-valid ng-touched">
        inputStr="//form[@class='ng-pristine ng-valid ng-touched']"
        volumePriceMenuElem = orderFormElem.find_elements_by_xpath(inputStr)[0]
            #     <div _ngcontent-ojc-c30="" class="order-form-field">
            #         <input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="1" max="undefined" step="5000" aria-valuemin="1" aria-valuemax="" aria-valuenow="5000" role="spinbutton">
        inputStr="//input[@class='dx-texteditor-input' @min='1']"
        volumeItemElem = orderFormElem.find_elements_by_xpath(inputStr)[0]
            
            #     <div _ngcontent-ojc-c30="" class="order-form-field mt-1">
            #         <input inputmode="decimal" autocomplete="off" class="dx-texteditor-input" type="text" spellcheck="false" min="undefined" max="undefined" step="25" aria-valuemin="" aria-valuemax="" aria-valuenow="5001" role="spinbutton">
        inputStr="//input[@class='dx-texteditor-input' @min='undefined']"
        priceItemElem = orderFormElem.find_elements_by_xpath(inputStr)[0]            
        #TODO 0 This Line next time    
            # کلید انجام عملیات یا پیشنویس        
            # <div _ngcontent-ojc-c30="" class="d-flex">
            #     <button _ngcontent-ojc-c30="" class="col-7 btn btn-sm btn-success flex-grow-1 px-0" title="(Enter)" type="submit"><!----><span _ngcontent-ojc-c30="">ارسال خرید</span><!----></button>
            #     <button _ngcontent-ojc-c30="" class="col btn btn-sm mr-1 px-0 btn-outline-warning" title="(Esc)" type="button">پیش&zwnj;نویس</button>
            
            # اطلاعات آماری منوی خرید و فروش
            # <div _ngcontent-ojc-c30="" class="mt-2 medium">   
            #     <div _ngcontent-ojc-c30="" class="row">
            #         <span _ngcontent-ojc-c30="" class="col-6 text-reverse-50">دارایی فعلی : </span>
            #         <span _ngcontent-ojc-c30="" class="col-6 text-start cup" dir="ltr">0</span>
            #     <div _ngcontent-ojc-c30="" class="row">
            #         <span _ngcontent-ojc-c30="" class="col-6 text-reverse-50">قیمت سر&zwnj;به&zwnj;سر: </span>
            #         <span _ngcontent-ojc-c30="" class="col-6 text-start" dir="ltr">53,122</span>

            #     <div _ngcontent-ojc-c30="" class="row">
            #         <span _ngcontent-ojc-c30="" class="col-6 text-reverse-50">هزینه معامله: </span>
            #         <span _ngcontent-ojc-c30="" class="col-6 text-start" dir="ltr">609,500</span>
            #     <div _ngcontent-ojc-c30="" class="row">
            #         <span _ngcontent-ojc-c30="" class="col-6 text-reverse-50">جمع کل:</span>
            #         <span _ngcontent-ojc-c30="" class="col-6 text-start" dir="ltr">530,609,500</span>
             
        pass

    def initializeSellSymbol(self):
        
        pass
    
    def fillBuySellForm(self):
        pass
    
    def DoneBuySellOperationNow():
        pass
       
    def lastCostSymbol(self):
        pass
    
    def rangeCostSymbol(self):
        pass
    
    def firstPriceSymbol(self):
        pass
    
    def sellQueueSymbol(self):
        pass
    
    def buyQueueSymbol(self):
        pass
    
    def buyAndSellPercentMaxDifSymbol(self):
        pass
    
    def buyAndSellPercentCurrentDifSymbol(self):
        pass
    
    def haghigiHoghogiDataSymbol(self):
        pass
    
    def efficiencyDaySymbol(self):
        pass
    
    def efficiencyWeekSymbol(self):
        pass    
    
    def efficiencyMonthSymbol(self):
        pass    
    

    
    
    

    def saveCookieToDB(self):
        pass

    def loadCookieFromDB(self):
        pass
        
    def testResponce(self):
        pass

    def closeChrome(self):
        del self.chrome