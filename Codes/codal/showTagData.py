from tinydb import TinyDB, Query
from tinydb import where
from CommonDefs import *
import logging                                                                  
import sys

import numpy as np
import matplotlib.pyplot as plt 


def showTag(symbol):
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.TagData,'symbol':symbol}))
    table = db.table("Main")
    tagDatas=table.all()
    
    data1=[]
    data2=[]
    data3=[]
    tagList=set({})
    dic={}
    for tagData in tagDatas:
        tagSimple=tagData["superSubject"]+':'+tagData["Subject"]+":"+str(tagData["duration"])
        if (tagData["Subject"].find("درآمدهای عملیاتی")==-1):
            continue
        tagList.add(tagSimple)
        if tagSimple in dic:
            dic[tagSimple]=dic[tagSimple]+1
        else:
            dic[tagSimple]=0
    
    database={}
    for tagData in tagDatas:
        tag=tagData["superSubject"]+':'+tagData["Subject"] #+":"+str(tagData["duration"])
        #if (tag.strip()==myTag):
        value=int(tagData["value"])
        hesabrasi=tagData["hesabrasi"]
        duration=int(tagData["duration"])
        date=str((tagData["date"]["year"]*10000)+(tagData["date"]["month"]*100)+(tagData["date"]["day"]))
        sendDate=str((tagData["sendDate"]["year"]*10000)+(tagData["sendDate"]["month"]*100)+(tagData["sendDate"]["day"]))
        normalValue=value/duration
        data1.append(date)
        data2.append(value)
        data3.append(normalValue)
        if not(tag in database):
            database[tag]={}
            database[tag]['date']=[]
            database[tag]['value']=[]
            database[tag]['normalValue']=[]
            database[tag]['hesabrasi']=[]
            database[tag]['title']=[]
        database[tag]['date'].append(date)
        database[tag]['value'].append(value)
        database[tag]['normalValue'].append(normalValue)
        database[tag]['hesabrasi'].append(int(hesabrasi))
        database[tag]['title'].append(\
            'd:'+str(date)+\
            ',m:'+str(tagData["duration"])+\
            ',h:'+str(int(hesabrasi))+\
            ', v:'+str(value)+\
            ',nV:'+str(normalValue)+\
            ',sD:'+str(sendDate)\
            )

    for tag in database:
        sortedDateIndex = np.lexsort((database[tag]['hesabrasi'], database[tag]['date']))    
        database[tag]['date'] = [database[tag]['date'][index] for index in sortedDateIndex]
        database[tag]['value'] = [database[tag]['value'][index] for index in sortedDateIndex]
        database[tag]['normalValue'] = [database[tag]['normalValue'][index] for index in sortedDateIndex]
        database[tag]['hesabrasi'] = [database[tag]['hesabrasi'][index] for index in sortedDateIndex]
        database[tag]['title'] = [database[tag]['title'][index] for index in sortedDateIndex]
    
    db.close()
    
    # f = open(FilenameManager.get({'enum':FilenameManager.Temp,'filename':"tagList.txt"}), "w", encoding="utf-8")
    # for i in tagList:
    #     f.write(i+"\n")     
    # f.close()
    
    import json
    f = open(FilenameManager.get({'enum':FilenameManager.Temp,'filename':"DicListTemp.json"}), "w", encoding="utf-8")
    jsonDatabase={}
    for tag in sorted (database):
        jsonDatabase[tag]=database[tag]['title']
    json.dump(jsonDatabase, f)
    f.close()

    counter=0
    for tag in tagList:
        if (counter==8):
            myTag=tag
        counter+=1
    
    myTag="سود -زیان خالص:درآمدهای عملیاتی"
    plt.xticks(  )
    x=database[myTag]['date']
    y=database[myTag]['normalValue']
    #ax = plt.subplots()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    
    plt.title(persianToFinglish(myTag))
    plt.text(10, 10, r'$\mu=100,\ \sigma=15$')
    #plt.axis([0, 20, 0, 20])
    # potting the points 
    #lines=plt.plot(x, y, dashes=[6, 2], label='Using the dashes parameter') 
    #plt.setp(lines, color='b', linewidth=2.0)
    #plt.annotate('local max', xy=(3, 5), xytext=(5, 10),
    #            arrowprops=dict(facecolor='black', shrink=0.05),
    #            )
    plt.scatter(x,  y, label='Using the Scatter parameter')
    #plt.bar(x,y, label='Using the Bar parameter')
    plt.legend()
    plt.show() 

def doOperation(symbol, symbolIndex, symbolsCounter):
    #todo: extract co list name and create folder for them 
    ## TrackNo_ValueNumber
    print("------"+persianToFinglish(symbol['sy']))        
    showTag(symbol['sy'])
    print("\n"+str(symbolIndex)+'/'+str(symbolsCounter)+":"+"-----")

def showTagData(start, end):
    timer = Timer()
    GroupProcess.getSymbols(start, end, True, doOperation)
    timer.printWatch()
    del timer
    
if __name__ == "__main__":
    showTagData(785,785)