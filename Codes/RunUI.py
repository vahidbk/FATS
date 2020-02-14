import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mofidBroker.easyTraderWidget import AppWindow

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())