from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *


def doOperation(symbol, symbolIndex, symbolsCounter):

    codalRawDataDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalRawData,'symbol':symbol['sy']}))
    soratMaliTableDataTable = codalRawDataDB.table('SoratHayeMali')
    soratMaliTableData = soratMaliTableDataTable.all()
    soratMaliTableDataLen = len(soratMaliTableData)
    
    CodalSoratMaliSheetIdDB = TinyDB(FilenameManager.get({'enum':FilenameManager.CodalSoratMaliSheetId}))
    SheetIDTable = CodalSoratMaliSheetIdDB.table('SheetID')
    SheetIDTableData = SheetIDTable.all()
    if not (SheetIDTableData):
        SheetIDTableData=set([])
    else:
        SheetIDTableData=set(SheetIDTableData[0]['Data'])
    
    for sorateMali in soratMaliTableData:
        sheetIds = sorateMali['theSubjectRecord']
        for sheetId in sheetIds:
            SheetIDTableData.add(sheetIds[sheetId]+" "+str(sheetId))
    CodalSoratMaliSheetIdDB.purge_table('SheetID')
    SheetIDTable = CodalSoratMaliSheetIdDB.table('SheetID')
    listSheetIDTableData = list(SheetIDTableData)
    listSheetIDTableData.sort()
    SheetIDTable.insert({'Data':listSheetIDTableData})
    
    CodalSoratMaliSheetIdDB.close()

def extractSubCoList(start, end):
    timer = Timer()
    GroupProcess.getSymbols(start, end, True, doOperation)
    timer.printWatch()
    del timer