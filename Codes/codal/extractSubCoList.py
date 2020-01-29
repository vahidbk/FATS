groupDB = TinyDB(FilenameManager.get({'enum':FilenameManager.Groups}))
corporations
symbolsTable = groupDB.table('Symbols')
symbols = symbolsTable.all()
symbolsCounter = len(symbols)
symbolIndex = 0;
startTime=datetime.now()
for symbol in symbols:
    symbolIndex+=1
    if not (symbol['GroupName']=='Unknown' or symbol['st']==2 or symbol['st']==3):
        print(str(symbolIndex)+'/'+str(symbolsCounter)+":"+symbol['sy'].strip())
        coList(symbol['sy'].strip()))
    else:
       print(str(symbolIndex)+'/'+str(symbolsCounter)+":"+"-----")
groupDB.close()
