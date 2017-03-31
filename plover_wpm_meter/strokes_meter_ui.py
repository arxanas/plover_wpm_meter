# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/waleedk/Workspace/plover_wpm_meter/plover_wpm_meter/strokes_meter.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StrokesMeter(object):
    def setupUi(self, StrokesMeter):
        StrokesMeter.setObjectName("StrokesMeter")
        StrokesMeter.resize(180, 151)
        self.layoutWidget = QtWidgets.QWidget(StrokesMeter)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 181, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.strokes_meter = QtWidgets.QGridLayout(self.layoutWidget)
        self.strokes_meter.setContentsMargins(0, 0, 0, 0)
        self.strokes_meter.setSpacing(0)
        self.strokes_meter.setObjectName("strokes_meter")
        self.strokes1 = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strokes1.sizePolicy().hasHeightForWidth())
        self.strokes1.setSizePolicy(sizePolicy)
        self.strokes1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.strokes1.setProperty("value", 0.0)
        self.strokes1.setObjectName("strokes1")
        self.strokes_meter.addWidget(self.strokes1, 0, 0, 1, 1)
        self.strokes1_label = QtWidgets.QLabel(self.layoutWidget)
        self.strokes1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.strokes1_label.setObjectName("strokes1_label")
        self.strokes_meter.addWidget(self.strokes1_label, 0, 1, 1, 1)
        self.strokes2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.strokes2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.strokes2.setProperty("value", 0.0)
        self.strokes2.setObjectName("strokes2")
        self.strokes_meter.addWidget(self.strokes2, 1, 0, 1, 1)
        self.strokes2_label = QtWidgets.QLabel(self.layoutWidget)
        self.strokes2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.strokes2_label.setObjectName("strokes2_label")
        self.strokes_meter.addWidget(self.strokes2_label, 1, 1, 1, 1)
        self.strokes_meter.setColumnStretch(0, 2)
        self.strokes_meter.setColumnStretch(1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(StrokesMeter)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 181, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.strokes_controls = QtWidgets.QGridLayout(self.layoutWidget1)
        self.strokes_controls.setContentsMargins(0, 0, 0, 0)
        self.strokes_controls.setSpacing(0)
        self.strokes_controls.setObjectName("strokes_controls")
        self.strokes_method = QtWidgets.QComboBox(self.layoutWidget1)
        self.strokes_method.setObjectName("strokes_method")
        self.strokes_controls.addWidget(self.strokes_method, 0, 0, 1, 1)

        self.retranslateUi(StrokesMeter)
        QtCore.QMetaObject.connectSlotsByName(StrokesMeter)

    def retranslateUi(self, StrokesMeter):
        _translate = QtCore.QCoreApplication.translate
        StrokesMeter.setWindowTitle(_translate("StrokesMeter", "Strokes Meter"))
        self.strokes1_label.setText(_translate("StrokesMeter", "last 10s"))
        self.strokes2_label.setText(_translate("StrokesMeter", "last 1m"))

