from CommonDefs import *
from codal.TagGeneratorSozAndZian import *
                

def doOperation(symbol, symbolIndex, symbolsCounter):
    #todo: extract co list name and create folder for them 
    ## TrackNo_ValueNumber
    print("------"+persianToFinglish(symbol['sy']))        
    tagGeneratorSozAndZian(symbol['sy'])
    print("\n"+str(symbolIndex)+'/'+str(symbolsCounter)+":"+"-----")

    
def processCodalDataToGenerateTags(start, end):
    timer = Timer()
    GroupProcess.getSymbols(start, end, True, doOperation)
    timer.printWatch()
    del timer

#processCodalDataToGenerateTags(785,785)