import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mofidBroker.easytraderdialog import Ui_Dialog
from mofidBroker.EasyTraderScraper import *

         
class AppWindow(QDialog):
    
    def computeGold(self):
        import threading
        from codal.Groups import updateGroups
        from gold.Gold import updateGoldData
        import json
        import time
        
        def goldComputeWorker():

            buttonList=[self.ui.pushButton_15, self.ui.pushButton_16, \
                self.ui.pushButton_17,self.ui.pushButton_18, \
                self.ui.pushButton_19, self.ui.pushButton_20, \
                self.ui.pushButton_21, self.ui.pushButton_22, \
                self.ui.pushButton_23,self.ui.pushButton_24]
            goldData=updateGoldData()
            buttonListCounter=0
            for key in goldData:
                buttonList[buttonListCounter].setText( key+":"+str(goldData[key]) )
                buttonListCounter+=1
            return

        t = threading.Thread(target=goldComputeWorker).start()
        
       
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        def ppp():
            print("1")
        self.easyTraderScraper = EasyTraderScraperClass() 
        self.ui.openChromeButton.clicked.connect(self.easyTraderScraper.openChrome)
        self.ui.openEasyTraderInChromeButton.clicked.connect(self.easyTraderScraper.openEasyTraderInChrome)
        self.ui.loginEasyTraderButton.clicked.connect(self.easyTraderScraper.loginEasyTrader)
        self.ui.loadEasyTraderButton.clicked.connect(self.easyTraderScraper.loadEasyTrader)
        self.ui.loadCookieFromDBButton.clicked.connect(self.easyTraderScraper.loadCookieFromDB)
        self.ui.testResponceButton.clicked.connect(self.easyTraderScraper.testResponce)
        self.ui.closeChromeButton.clicked.connect(self.easyTraderScraper.closeChrome)
        
        self.ui.computeGoldButton.clicked.connect(self.computeGold)
        self.ui.closeSearchMenuButton.clicked.connect(self.easyTraderScraper.closeSearchMenu)
        self.ui.focusOnSymbolButton.clicked.connect(self.easyTraderScraper.focusOnSymbol)
        
        self.ui.startBuySymbolButton.clicked.connect(self.easyTraderScraper.startBuySymbol)
        self.ui.startSellSymbolButton.clicked.connect(self.easyTraderScraper.startSellSymbol)


        self.ui.pushButton_15.clicked.connect(self.computeGold)
        
        self.show() 
        
        

