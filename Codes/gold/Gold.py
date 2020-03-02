from bs4 import BeautifulSoup
import requests.packages.urllib3
import jsons
import time
from datetime import datetime
from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import urllib.request
import threading 


def getOns():
    try:
        requests.packages.urllib3.disable_warnings()
        url="https://www.kitco.com/charts/livegold.html"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(url, headers=headers, verify = False, timeout=(10, 20))
        soup = BeautifulSoup(response.text,"lxml")
        div = soup.find_all('span', attrs={'id':'sp-bid'})[0]
        ons=persianStrToInt(div.get_text(strip=True, separator=',').replace("\n", ""))
        return {'ons':ons}
    except Exception as err:
        print(f'Other error occurred IN Connection To get Ons: {err}') 


def getGold():
    try:
        requests.packages.urllib3.disable_warnings()
        url="https://www.tala.ir/price/18k"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(url, headers=headers, verify = False, timeout=(10, 20))
        soup = BeautifulSoup(response.text,"lxml")
        divs = soup.find_all('div', attrs={'class':'col-xs-12'})
        h3 = divs[9].find('h3')
        lastPrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        h3 = divs[11].find('h3')
        maxPrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        h3 = divs[13].find('h3')
        minPrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        h3 = divs[15].find('h3')
        yesterdayClosePrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        h3 = divs[17].find('h3')
        yesterdaMaxPrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        h3 = divs[19].find('h3')
        yesterdayMinPrice=persianStrToInt(h3.get_text(strip=True, separator=',').replace("\n", ""))
        return {'goldLastPrice':lastPrice, 'goldMaxPrice':maxPrice, 'goldMinPrice':minPrice, \
                'GoldYesterdayClosePrice':yesterdayClosePrice, 'goldYesterdayMaxPrice':yesterdaMaxPrice, 'goldYesterdayMinPrice':yesterdayMinPrice}
    except Exception as err:
        print(f'Other error occurred IN Connection To get Ons: {err}') 

def getDolar():
    pass
    
def ComputeGold(dolar, myounce):
    try:
        requests.packages.urllib3.disable_warnings()
        url="https://amoozesh.org/gold/dollar.php"
        response = requests.post(url, {"mydollar":dolar, "myounce":myounce, "isdollar":1} , verify = False, timeout=(10, 20))
        soup = BeautifulSoup(response.text,"lxml")
        div = soup.find_all('div')
        goldSpan = div[0].find_all('span')[1]
        gold = persianStrToInt(goldSpan.get_text(strip=True, separator=',').replace("\n", ""))
        sekeSpan = div[1].find_all('span')[1]
        seke = persianStrToInt(sekeSpan.get_text(strip=True, separator=',').replace("\n", ""))
        gold = (float(gold)/4.3318)
        seke = float(seke)
        return {'gold':gold, 'seke':seke}
    except Exception as err:
        print(f'Other error occurred IN Connection for Formula: {err}') 
 
def updateGoldData():        
    ons = getOns()
    gold = getGold()
    GoldWithDolarEqualOne = ComputeGold(1, ons['ons'])
    dolar = float(gold['goldLastPrice'])/GoldWithDolarEqualOne['gold']
    GoldWithDolarLast = ComputeGold(dolar, ons['ons'])
    result = {}
    for key,value in ons.items():
        result[key]=value
    for key,value in gold.items():
        result[key]=value
    for key,value in GoldWithDolarLast.items():
        result[key]=value 
    result['dolar']=dolar
    return result

