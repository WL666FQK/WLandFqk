# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 29, 571, 471))
        self.groupBox.setObjectName("groupBox")
        self.ImageLabel = QtWidgets.QLabel(self.groupBox)
        self.ImageLabel.setGeometry(QtCore.QRect(30, 30, 301, 351))
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.OpenFileBtn = QtWidgets.QPushButton(self.groupBox)
        self.OpenFileBtn.setGeometry(QtCore.QRect(380, 50, 151, 71))
        self.OpenFileBtn.setObjectName("OpenFileBtn")
        self.infoLabel = QtWidgets.QLabel(self.groupBox)
        self.infoLabel.setGeometry(QtCore.QRect(10, 410, 541, 51))
        self.infoLabel.setObjectName("infoLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionexit)
        self.menu_2.addAction(self.actionabout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片浏览器"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.OpenFileBtn.setText(_translate("MainWindow", "打开文件"))
        self.infoLabel.setText(_translate("MainWindow", "欢迎使用该软件"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionOpen.setText(_translate("MainWindow", "打开文件"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
