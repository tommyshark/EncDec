# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 330)
        MainWindow.setMinimumSize(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Загрузки/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 500, 91, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(340, 90, 91, 34))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnEncrypt.setFont(font)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(340, 210, 91, 34))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDecrypt.setFont(font)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 321, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(440, 70, 321, 201))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Armenian Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 280, 81, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 161, 32))
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(340, 150, 91, 34))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EncDec"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_4.setText(_translate("MainWindow", "EncDec"))
        self.label_5.setText(_translate("MainWindow", "version"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Not set"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Base64"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Base32"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Base16"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Base85"))
        self.comboBox.setItemText(5, _translate("MainWindow", "URL"))
        self.comboBox.setItemText(6, _translate("MainWindow", "URL fully"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Reverser"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Hex"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Binary"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Caesar"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Xml/Html encoding"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
