# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flasher.ui'
#
# Created: Tue Mar  6 17:50:25 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Flasher(object):
    def setupUi(self, Flasher):
        Flasher.setObjectName("Flasher")
        Flasher.resize(553, 460)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Flasher.sizePolicy().hasHeightForWidth())
        Flasher.setSizePolicy(sizePolicy)
        Flasher.setMinimumSize(QtCore.QSize(553, 460))
        Flasher.setMaximumSize(QtCore.QSize(553, 460))
        self.lineFile = QtGui.QLineEdit(Flasher)
        self.lineFile.setGeometry(QtCore.QRect(20, 30, 451, 27))
        self.lineFile.setObjectName("lineFile")
        self.buttonLoad = QtGui.QPushButton(Flasher)
        self.buttonLoad.setGeometry(QtCore.QRect(480, 30, 51, 27))
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonExec = QtGui.QPushButton(Flasher)
        self.buttonExec.setGeometry(QtCore.QRect(20, 110, 511, 41))
        self.buttonExec.setObjectName("buttonExec")
        self.textOut = QtGui.QPlainTextEdit(Flasher)
        self.textOut.setGeometry(QtCore.QRect(20, 210, 511, 211))
        self.textOut.setReadOnly(True)
        self.textOut.setObjectName("textOut")
        self.progressBar = QtGui.QProgressBar(Flasher)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label = QtGui.QLabel(Flasher)
        self.label.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Flasher)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label_2.setObjectName("label_2")
        self.saveLog = QtGui.QPushButton(Flasher)
        self.saveLog.setGeometry(QtCore.QRect(300, 430, 231, 23))
        self.saveLog.setObjectName("saveLog")
        self.boardGroup = QtGui.QGroupBox(Flasher)
        self.boardGroup.setEnabled(False)
        self.boardGroup.setGeometry(QtCore.QRect(20, 60, 511, 41))
        self.boardGroup.setTitle("")
        self.boardGroup.setObjectName("boardGroup")
        self.spartan6Board = QtGui.QRadioButton(self.boardGroup)
        self.spartan6Board.setGeometry(QtCore.QRect(0, 20, 141, 22))
        self.spartan6Board.setChecked(True)
        self.spartan6Board.setObjectName("spartan6Board")
        self.label_3 = QtGui.QLabel(self.boardGroup)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 271, 17))
        self.label_3.setObjectName("label_3")
        self.virtex6Board1 = QtGui.QRadioButton(self.boardGroup)
        self.virtex6Board1.setGeometry(QtCore.QRect(140, 20, 141, 22))
        self.virtex6Board1.setObjectName("virtex6Board1")

        self.retranslateUi(Flasher)
        QtCore.QMetaObject.connectSlotsByName(Flasher)

    def retranslateUi(self, Flasher):
        Flasher.setWindowTitle(QtGui.QApplication.translate("Flasher", "XSVFPlay FPGA Programming Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoad.setText(QtGui.QApplication.translate("Flasher", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExec.setText(QtGui.QApplication.translate("Flasher", "Start FPGA Programming", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Flasher", "Console Output :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Flasher", "Select .xsvf File :", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLog.setText(QtGui.QApplication.translate("Flasher", "Save Output Log...", None, QtGui.QApplication.UnicodeUTF8))
        self.spartan6Board.setText(QtGui.QApplication.translate("Flasher", "SPARTAN6 Board", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Flasher", "Select Target FPGA Board :", None, QtGui.QApplication.UnicodeUTF8))
        self.virtex6Board1.setText(QtGui.QApplication.translate("Flasher", "VIRTEX6 Board 1.0", None, QtGui.QApplication.UnicodeUTF8))

