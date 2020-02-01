import jsons
import requests
from bs4 import BeautifulSoup
from tinydb import Query, TinyDB, where
from CommonDefs import *

def updateGroups():
    requests.packages.urllib3.disable_warnings()

    db = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
    response = requests.get('http://www.tsetmc.com/Loader.aspx?ParTree=111C1213',verify = False)
    soup = BeautifulSoup(response.text,"lxml")
    tds = soup.find_all({'td'})
    jsonGroupDatas=[]
    groupDict={}
    for i in range(1, int(len(tds)/2)):
        jsonGroupDatas.append({'code':(tds[0+(2*i)].text.strip()) , 'name':(tds[1+(2*i)].text.strip())})
        groupDict[(tds[0+(2*i)].text.strip())]=(tds[1+(2*i)].text.strip())
    db.purge_table('Groups')
    groupTable = db.table('Groups')
    groupTable.insert_multiple(jsonGroupDatas)
    print('Groups Done')
    #----------
    response = requests.get('https://search.codal.ir/api/search/v1/categories',verify = False)
    db.purge_table('Categories')
    categoriesTable = db.table('Categories')
    categoriesTable.insert_multiple(response.json())
    print('Categories Done')
    #----------
    response = requests.get('https://search.codal.ir/api/search/v1/companies',verify = False)
    jsonDatas = response.json()
    for jsonData in jsonDatas:
        code = jsonData["i"][:2]
        jsonData['Group'] = code
        if code in groupDict:
            jsonData['GroupName'] = groupDict[code]
        else:
            jsonData['GroupName'] = 'Unknown'
    db.purge_table('Symbols')
    symbolsTable = db.table('Symbols')
    symbolsTable.insert_multiple(jsonDatas)
    print('Symbols Done')
    #----------
    symbolsTable = db.table('Symbols')
    symbols = symbolsTable.all()
    symbolGroupByGroupName={}
    for symbol in symbols:
        if not (symbol['GroupName'] in symbolGroupByGroupName):
            symbolGroupByGroupName[symbol['GroupName']]={}
        symbolGroupByGroupName[symbol['GroupName']][symbol['sy']]=symbol['n']
    db.purge_table('SymbolGroupByGroupName')    
    symbolsTable = db.table('SymbolGroupByGroupName')
    symbolsTable.insert(symbolGroupByGroupName)    
    #----------
    totalSymbolInGroup={}
    for groupName in symbolGroupByGroupName:
        symbolInGroupCounter=len(symbolGroupByGroupName[groupName])
        totalSymbolInGroup[groupName]=symbolInGroupCounter
    db.purge_table('totalSymbolInGroup')    
    symbolsTable = db.table('totalSymbolInGroup')
    symbolsTable.insert(totalSymbolInGroup)    
    #----------
    print('Processing on Data is Done')
    db.close()
