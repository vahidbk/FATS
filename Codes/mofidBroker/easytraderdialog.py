# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../FATS\Codes\mofidBroker\easytraderdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 10, 170, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.openChromeButton = QtWidgets.QPushButton(self.widget)
        self.openChromeButton.setObjectName("openChromeButton")
        self.verticalLayout_2.addWidget(self.openChromeButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.openEasyTraderInChromeButton = QtWidgets.QPushButton(self.widget)
        self.openEasyTraderInChromeButton.setObjectName("openEasyTraderInChromeButton")
        self.verticalLayout.addWidget(self.openEasyTraderInChromeButton)
        self.loginEasyTraderButton = QtWidgets.QPushButton(self.widget)
        self.loginEasyTraderButton.setObjectName("loginEasyTraderButton")
        self.verticalLayout.addWidget(self.loginEasyTraderButton)
        self.saveCookieToDBButton = QtWidgets.QPushButton(self.widget)
        self.saveCookieToDBButton.setObjectName("saveCookieToDBButton")
        self.verticalLayout.addWidget(self.saveCookieToDBButton)
        self.loadCookieFromDBButton = QtWidgets.QPushButton(self.widget)
        self.loadCookieFromDBButton.setObjectName("loadCookieFromDBButton")
        self.verticalLayout.addWidget(self.loadCookieFromDBButton)
        self.testResponceButton = QtWidgets.QPushButton(self.widget)
        self.testResponceButton.setObjectName("testResponceButton")
        self.verticalLayout.addWidget(self.testResponceButton)
        self.closeChromeButton = QtWidgets.QPushButton(self.widget)
        self.closeChromeButton.setObjectName("closeChromeButton")
        self.verticalLayout.addWidget(self.closeChromeButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.openChromeButton.setText(_translate("Dialog", "openChrome"))
        self.openEasyTraderInChromeButton.setText(_translate("Dialog", "openEasyTraderInChrome"))
        self.loginEasyTraderButton.setText(_translate("Dialog", "autoLoginEasyTrader"))
        self.saveCookieToDBButton.setText(_translate("Dialog", "EasyTrader"))
        self.loadCookieFromDBButton.setText(_translate("Dialog", "getRemainMoneyByCode"))
        self.testResponceButton.setText(_translate("Dialog", "testResponce"))
        self.closeChromeButton.setText(_translate("Dialog", "closeChrome"))
