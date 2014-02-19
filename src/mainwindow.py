# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Thu Feb 20 01:09:11 2014
#      by: PyQt4 UI code generator 4.10.3
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
        MainWindow.resize(546, 307)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 20, 191, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 174, 174))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.videoPlay = QtGui.QPushButton(self.layoutWidget)
        self.videoPlay.setMinimumSize(QtCore.QSize(80, 80))
        self.videoPlay.setAutoDefault(True)
        self.videoPlay.setDefault(True)
        self.videoPlay.setObjectName(_fromUtf8("videoPlay"))
        self.gridLayout.addWidget(self.videoPlay, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 301, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 32, 258, 166))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.songNum = QtGui.QSpinBox(self.layoutWidget1)
        self.songNum.setProperty("value", 15)
        self.songNum.setObjectName(_fromUtf8("songNum"))
        self.horizontalLayout_3.addWidget(self.songNum)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(166, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.songPattern = QtGui.QLineEdit(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songPattern.sizePolicy().hasHeightForWidth())
        self.songPattern.setSizePolicy(sizePolicy)
        self.songPattern.setMinimumSize(QtCore.QSize(200, 0))
        self.songPattern.setObjectName(_fromUtf8("songPattern"))
        self.horizontalLayout.addWidget(self.songPattern)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(166, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.songPlay = QtGui.QPushButton(self.layoutWidget1)
        self.songPlay.setMinimumSize(QtCore.QSize(80, 50))
        self.songPlay.setAutoDefault(True)
        self.songPlay.setObjectName(_fromUtf8("songPlay"))
        self.horizontalLayout_2.addWidget(self.songPlay)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 546, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionConfig = QtGui.QAction(MainWindow)
        self.actionConfig.setObjectName(_fromUtf8("actionConfig"))
        self.action_db_update = QtGui.QAction(MainWindow)
        self.action_db_update.setObjectName(_fromUtf8("action_db_update"))
        self.menuFile.addAction(self.actionConfig)
        self.menuFile.addAction(self.action_db_update)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.songPattern, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.songPlay.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "My Random Player", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Movie", None))
        self.videoPlay.setText(_translate("MainWindow", "Play", None))
        self.groupBox.setTitle(_translate("MainWindow", "Music", None))
        self.label.setText(_translate("MainWindow", "Song Number: ", None))
        self.label_2.setText(_translate("MainWindow", "Search: ", None))
        self.songPlay.setText(_translate("MainWindow", "Play", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionConfig.setText(_translate("MainWindow", "Config", None))
        self.action_db_update.setText(_translate("MainWindow", "Update Music Database", None))

