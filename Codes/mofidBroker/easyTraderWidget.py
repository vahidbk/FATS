import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mofidBroker.easytraderdialog import Ui_Dialog
from mofidBroker.EasyTraderScraper import *

class AppWindow(QDialog):
    
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
        self.ui.saveCookieToDBButton.clicked.connect(self.easyTraderScraper.saveCookieToDB)
        self.ui.loadCookieFromDBButton.clicked.connect(self.easyTraderScraper.loadCookieFromDB)
        self.ui.testResponceButton.clicked.connect(self.easyTraderScraper.testResponce)
        self.ui.closeChromeButton.clicked.connect(self.easyTraderScraper.closeChrome)
        
        self.show()  

