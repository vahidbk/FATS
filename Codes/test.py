
from CommonDefs import *
from requestium import Session, Keys

options = {'--log-level':'3', 'user-data-dir':FilenameManager.get({'enum':FilenameManager.ChromeProfile}), \
        'default_timeout':'15','browser':'chrome'}

options = {'--log-level':'3', 'user-data-dir':FilenameManager.get({'enum':FilenameManager.ChromeProfile})}

s = Session(webdriver_path='D:/Desktop/بورس/04-pyton/chromedriver_win32/chromedriver.exe', \
            browser='chrome',\
            default_timeout=15,\
            webdriver_options=options)
title = s.get('http://google.com')
s.transfer_session_cookies_to_driver()  # You can mantain the session if needed
s.driver.get('http://www.yahoo.com ')
s.transfer_driver_cookies_to_session()
s.post('http://www.google.com/', data={'key1': 'value1'}) 
s.get('http://www.google.com/') 
s.options('http://www.google.com/') 
exit(0)


# from seleniumrequests import Chrome
# #options = webdriver.ChromeOptions()
# #options.add_argument("--log-level=3");
# #options.add_argument() #Path to your chrome profile
# chromeWebDriverPath = 'D:/Desktop/بورس/04-pyton/chromedriver_win32/chromedriver.exe'
# webdriver = Chrome(executable_path=chromeWebDriverPath)
# #webdriver = webdriver.Chrome(executable_path=chromeWebDriverPath, options=options)
            
# # Simple usage with built-in WebDrivers:
# response = webdriver.request('GET', 'https://www.google.com/')
# print(response)
# print(response.content)


# from CommonDefs import *

# from codal.extractSubCoList import extractSubCoList
# start = 786
# end = 786
# extractSubCoList(start, end)
