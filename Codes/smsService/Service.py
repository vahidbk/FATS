import time
from smsService.ModemConnection import *
from tinydb import TinyDB, Query
from CommonDefs import *

personal = "Personal"
try:
    db = TinyDB(FilenameManager.get({'enum':FilenameManager.LoginData}))
    userTable = db.table(personal)
    user = userTable.all()
    ValidPhoneNumber=user[0]["PhoneNumber"]
    db.close()
except:
    print("Error in username and password Easy Trader.")
    db.purge_table(personal)
    userTable = db.table(personal)
    userTable.insert({"PhoneNumber":"TypePhoneNumberHere"})
    db.close()


def onSmsReceived(sms):
    #sms.number, sms.time, sms.text
    #From: +98936XXX9014
    #Time: 2020-01-23 08:04:11+03:30
    if sms.number==ValidPhoneNumber:
        commands = sms.text.split('%')
        for command in commands:
            if command=='گ':
                from Gold import updateGoldData
                goldPrice=updateGoldData()
                message=""
                message+="طلا "+str(goldPrice['gold'])+'\n'
                message+="انس "+str(goldPrice['ons'])+'\n'
                message+="سکه "+str(goldPrice['seke'])+'\n'
                #message+=u"اعتبار "+str(connection.getIrancellAccountBalance())
                sms.reply(message)                
        
def main():
    connection = phoneConnection(onSmsReceived)
    while(True):
        time.sleep(1)
    del connection
    print("accountBalance:"+str(connection.getIrancellAccountBalance()))

if __name__ == '__main__':
    #print(updateGoldData())
    main()
    