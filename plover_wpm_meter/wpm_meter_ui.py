# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/waleed/Workspace/python/plover_wpm_meter/plover_wpm_meter/wpm_meter.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WpmMeter(object):
    def setupUi(self, WpmMeter):
        WpmMeter.setObjectName("WpmMeter")
        WpmMeter.resize(182, 120)
        self.centralWidget = QtWidgets.QWidget(WpmMeter)
        self.centralWidget.setGeometry(QtCore.QRect(30, 0, 100, 30))
        self.centralWidget.setObjectName("centralWidget")
        self.wpm1 = QtWidgets.QLCDNumber(WpmMeter)
        self.wpm1.setGeometry(QtCore.QRect(0, 0, 121, 61))
        self.wpm1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.wpm1.setProperty("value", 0.0)
        self.wpm1.setObjectName("wpm1")
        self.wpm2 = QtWidgets.QLCDNumber(WpmMeter)
        self.wpm2.setGeometry(QtCore.QRect(0, 60, 121, 61))
        self.wpm2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.wpm2.setProperty("value", 0.0)
        self.wpm2.setObjectName("wpm2")
        self.label = QtWidgets.QLabel(WpmMeter)
        self.label.setGeometry(QtCore.QRect(130, 20, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(WpmMeter)
        self.label_2.setGeometry(QtCore.QRect(130, 80, 51, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(WpmMeter)
        QtCore.QMetaObject.connectSlotsByName(WpmMeter)

    def retranslateUi(self, WpmMeter):
        _translate = QtCore.QCoreApplication.translate
        WpmMeter.setWindowTitle(_translate("WpmMeter", "WPM Meter"))
        self.label.setText(_translate("WpmMeter", "last 10s"))
        self.label_2.setText(_translate("WpmMeter", "last 1m"))

