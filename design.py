# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(602, 689)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.source1 = QtGui.QLineEdit(self.centralwidget)
        self.source1.setObjectName(_fromUtf8("source1"))
        self.verticalLayout.addWidget(self.source1)
        self.source1btn = QtGui.QPushButton(self.centralwidget)
        self.source1btn.setObjectName(_fromUtf8("source1btn"))
        self.verticalLayout.addWidget(self.source1btn)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.destination1 = QtGui.QLineEdit(self.centralwidget)
        self.destination1.setObjectName(_fromUtf8("destination1"))
        self.verticalLayout.addWidget(self.destination1)
        self.destination1btn = QtGui.QPushButton(self.centralwidget)
        self.destination1btn.setObjectName(_fromUtf8("destination1btn"))
        self.verticalLayout.addWidget(self.destination1btn)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.analysisBtn = QtGui.QRadioButton(self.centralwidget)
        self.analysisBtn.setChecked(True)
        self.analysisBtn.setObjectName(_fromUtf8("analysisBtn"))
        self.verticalLayout.addWidget(self.analysisBtn)
        self.processingBtn = QtGui.QRadioButton(self.centralwidget)
        self.processingBtn.setChecked(False)
        self.processingBtn.setObjectName(_fromUtf8("processingBtn"))
        self.verticalLayout.addWidget(self.processingBtn)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.filesonlyBtn = QtGui.QCheckBox(self.centralwidget)
        self.filesonlyBtn.setObjectName(_fromUtf8("filesonlyBtn"))
        self.verticalLayout.addWidget(self.filesonlyBtn)
        self.exportAllBtn = QtGui.QCheckBox(self.centralwidget)
        self.exportAllBtn.setObjectName(_fromUtf8("exportAllBtn"))
        self.verticalLayout.addWidget(self.exportAllBtn)
        self.resforksBtn = QtGui.QCheckBox(self.centralwidget)
        self.resforksBtn.setObjectName(_fromUtf8("resforksBtn"))
        self.verticalLayout.addWidget(self.resforksBtn)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.process = QtGui.QPushButton(self.centralwidget)
        self.process.setObjectName(_fromUtf8("process"))
        self.verticalLayout.addWidget(self.process)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Disk Image Processor", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.source1.setPlaceholderText(_translate("MainWindow", "/path/to/source", None))
        self.source1btn.setText(_translate("MainWindow", "Browse", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Destination</span></p></body></html>", None))
        self.destination1.setPlaceholderText(_translate("MainWindow", "/path/to/destination", None))
        self.destination1btn.setText(_translate("MainWindow", "Browse", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mode</span></p></body></html>", None))
        self.analysisBtn.setText(_translate("MainWindow", "Analysis", None))
        self.processingBtn.setText(_translate("MainWindow", "Processing", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Processing Mode options</span></p></body></html>", None))
        self.checkBox.setText(_translate("MainWindow", "Bag SIPs", None))
        self.filesonlyBtn.setText(_translate("MainWindow", "Make SIPs from logical files only (no disk images)", None))
        self.exportAllBtn.setText(_translate("MainWindow", "Export all files with tsk_recover (not only allocated)", None))
        self.resforksBtn.setText(_translate("MainWindow", "Export AppleDouble resource forks from HFS-formatted disks", None))
        self.checkBox_3.setText(_translate("MainWindow", "Run bulk_extractor", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Detailed output</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>", None))
        self.process.setText(_translate("MainWindow", "Process disk images", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setToolTip(_translate("MainWindow", "<html><head/><body><p>About Disk Image Processor</p></body></html>", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))

