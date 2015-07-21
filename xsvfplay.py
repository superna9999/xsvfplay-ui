#!/usr/bin/python
#
# XSVFPlay flasher manager
#   Manage flasher database
#
# Copyright (C) Superna 2015
#

import sys
import os
import subprocess
import shlex
import random
import re
from PyQt4 import QtCore, QtGui
from ui import 	*
from Queue import Queue, Empty
from threading import Thread

def print_lines(out, q):
	for line in iter(out.readline, b''):
		q.put(line)
	print("close")
	out.close()

class MainWindow(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)

        self.ui = Ui_Flasher()
        self.ui.setupUi(self)
		
        self.ui.buttonExec.setEnabled(False)
        
        self.process = QtCore.QProcess(self)
        self.process.finished.connect(self.onFinished)
        self.process.started.connect(self.onStarted)
        self.process.readyReadStandardOutput.connect(self.printOutput)
        self.process.readyReadStandardError.connect(self.printErrors)

    def on_saveLog_pressed(self):
        f = QtGui.QFileDialog.getSaveFileName(self, 'Select a file', '.', 'Log File (*.log)')
        if len(f):
            file = open(f, 'w+')
            file.write(self.ui.textOut.toPlainText())
            file.close()

    def on_buttonLoad_pressed(self):
        f = QtGui.QFileDialog.getOpenFileName(self, 'Select a file', '.', 'Flasher file (*.xsvf)')
        if len(f):
            self.ui.lineFile.setText(f)
            self.ui.buttonExec.setEnabled(True)
            self.ui.boardGroup.setEnabled(True)
        else:
			return

    def on_lineText_changed(self):
        self.ui.textOut.clear()

    def onFinished(self, exitCode, exitStatus):
		self.ui.buttonExec.setEnabled(True)
		self.ui.buttonLoad.setEnabled(True)
		self.ui.boardGroup.setEnabled(True)
		if exitCode <> 0:
			self.ui.textOut.appendPlainText("Failed !!!")
		else:
			self.ui.textOut.appendPlainText("Finished")
	   
    def onStarted(self):
		self.ui.buttonExec.setEnabled(False)
		self.ui.buttonLoad.setEnabled(False)
		self.ui.boardGroup.setEnabled(False)
		self.ui.textOut.appendPlainText("Started")
	
    def printOutput(self):
		regex = re.compile('\[ *(\d+)%\]')
		lines = self.process.readAllStandardOutput().data()
		line = re.split("\r", lines)
		for l in line:
			if regex.search(l) <> None:
				self.ui.progressBar.setValue(int(regex.search(l).group(1)))
		self.ui.textOut.appendPlainText(lines)

    def printErrors(self):
		lines = self.process.readAllStandardError().data()
		self.ui.textOut.appendPlainText(lines)

    def on_buttonExec_pressed(self):
        root = os.path.abspath(os.path.dirname(sys.argv[0]))

        print root

        if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
            command = root + "\\xsvfplay.exe"
        elif sys.platform.startswith('linux'):
            command = root + "/xsvfplay"
        else:
            self.ui.textOut.appendPlainText("System not supported !")

        print command

        if self.ui.spartan6Board.isChecked():
            args = ["-p", "-x", self.ui.lineFile.text()]
        elif self.ui.virtex6Board1.isChecked():
            args = ["-p", "-n", "-J", "Quad RS232-HS B", "-x", self.ui.lineFile.text()]
        else:
            self.ui.textOut.appendPlainText("Board not supported !")

        print args

        #if command and args:
        self.process.start(command, args)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
