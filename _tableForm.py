# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableProducts = QtWidgets.QListWidget(self.centralwidget)
        self.tableProducts.setGeometry(QtCore.QRect(10, 10, 251, 201))
        self.tableProducts.setObjectName("tableProducts")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 30, 201, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txtprice = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtprice.setObjectName("txtprice")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtprice)
        self.txtname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtname.setObjectName("txtname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtname)
        self.lblname = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblname.setObjectName("lblname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblname)
        self.lblprice = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblprice.setObjectName("lblprice")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblprice)
        self.btnSave = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnSave.setObjectName("btnSave")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnSave)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblname.setText(_translate("MainWindow", "Name:"))
        self.lblprice.setText(_translate("MainWindow", "Price:"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
