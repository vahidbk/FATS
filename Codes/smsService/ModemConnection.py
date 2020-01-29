from __future__ import print_function
import logging
from gsmmodem.modem import GsmModem
import binascii
import serial.tools.list_ports

class phoneConnection:
    def __init__(self, handleSMSCallBack):
        self.port = '/dev/ttyUSB2'
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'ZTE NMEA Device' in p.description:
                self.port=p.device
        self.baudRate = 115200
        self.pin = None # SIM card PIN (if any)
        self.modem = GsmModem(self.port, self.baudRate, smsReceivedCallbackFunc=handleSMSCallBack\
            ,incomingCallCallbackFunc=handleCall)
        self.modem.smsTextMode=False
        self.modem.connect(self.pin)
        self.signalStrength=self.modem.waitForNetworkCoverage(10)
        self.response=None
        self.modem.ownNumber
    def sendUSSD(self, ussdString):
        if (self.response and self.response.sessionActive):
            self.response.reply(ussdString) 
        else:
            self.response = self.modem.sendUssd(ussdString)
        ucs2Message=binascii.unhexlify(self.response.message)
        utf16Message=ucs2Message.decode('utf-16-be')
        return utf16Message
        
    def sessionActiveClose(self):
        if self.response.sessionActive:
            response.cancel()
    
    def getIrancellAccountBalance(self):
        try:
            message=self.sendUSSD('*141*1#')
            balance=int(message.split()[1])
            self.sessionActiveClose()
        except:
            balance=-1
        return balance
    
    def accountCharging(self):
        pass
        #'*780*2*1*0936XXX9014*10000*1*#')
                
    def __del__(self):
        if (self.modem):
            self.modem.close()
   
''' if __name__ == '__main__':
    connection = phoneConnection()
    print("accountBalance:"+str(connection.getIrancellAccountBalance()))
    del phoneConnection
 '''


def handleCall():
    print("call")
    
def handleSms(sms):
    #sms.number, sms.time, sms.text
    #From: +989364299014
    #Time: 2020-01-23 08:04:11+03:30
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
    print('Replying to SMS...')
    sms.reply(u'SMS received: "{0}{1}"'.format(sms.text[:20], '...' if len(sms.text) > 20 else ''))
    print('SMS sent.\n')

def main():
    connection = phoneConnection(handleSms)
    print('Waiting for SMS message...')
    import time
    time.sleep(100)
    del connection

if __name__ == '__main__':
    main()
    
    
