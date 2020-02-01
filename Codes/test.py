from CommonDefs import *

from codal.extractSubCoList import extractSubCoList
start = 786
end = 786
extractSubCoList(start, end)





exit(0)

from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
