# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 260)
        self.txtIn = QtWidgets.QTextEdit(Dialog)
        self.txtIn.setGeometry(QtCore.QRect(10, 10, 530, 70))
        self.txtIn.setObjectName("txtIn")
        self.txtOut = QtWidgets.QTextEdit(Dialog)
        self.txtOut.setGeometry(QtCore.QRect(10, 150, 530, 70))
        self.txtOut.setObjectName("txtOut")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 230, 537, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbUpper = QtWidgets.QCheckBox(self.widget)
        self.cbUpper.setObjectName("cbUpper")
        self.horizontalLayout.addWidget(self.cbUpper)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cbMulti = QtWidgets.QCheckBox(self.widget)
        self.cbMulti.setObjectName("cbMulti")
        self.horizontalLayout.addWidget(self.cbMulti)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cbFrame = QtWidgets.QCheckBox(self.widget)
        self.cbFrame.setObjectName("cbFrame")
        self.horizontalLayout.addWidget(self.cbFrame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cbCentered = QtWidgets.QCheckBox(self.widget)
        self.cbCentered.setObjectName("cbCentered")
        self.horizontalLayout.addWidget(self.cbCentered)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cbCopy = QtWidgets.QCheckBox(self.widget)
        self.cbCopy.setObjectName("cbCopy")
        self.horizontalLayout.addWidget(self.cbCopy)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.cbAlways = QtWidgets.QCheckBox(self.widget)
        self.cbAlways.setObjectName("cbAlways")
        self.horizontalLayout.addWidget(self.cbAlways)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 531, 52))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnMakeComment = QtWidgets.QPushButton(self.widget1)
        self.btnMakeComment.setObjectName("btnMakeComment")
        self.horizontalLayout_3.addWidget(self.btnMakeComment)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btnCopy = QtWidgets.QPushButton(self.widget1)
        self.btnCopy.setObjectName("btnCopy")
        self.horizontalLayout_3.addWidget(self.btnCopy)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gbLang = QtWidgets.QGroupBox(self.widget1)
        self.gbLang.setObjectName("gbLang")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbLang)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbPython = QtWidgets.QRadioButton(self.gbLang)
        self.rbPython.setObjectName("rbPython")
        self.horizontalLayout_2.addWidget(self.rbPython)
        self.rbC = QtWidgets.QRadioButton(self.gbLang)
        self.rbC.setObjectName("rbC")
        self.horizontalLayout_2.addWidget(self.rbC)
        self.rbMatlab = QtWidgets.QRadioButton(self.gbLang)
        self.rbMatlab.setObjectName("rbMatlab")
        self.horizontalLayout_2.addWidget(self.rbMatlab)
        self.horizontalLayout_3.addWidget(self.gbLang)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cbUpper.setText(_translate("Dialog", "All uppercase"))
        self.cbMulti.setText(_translate("Dialog", "Multilines"))
        self.cbFrame.setText(_translate("Dialog", "Frame"))
        self.cbCentered.setText(_translate("Dialog", "Centered"))
        self.cbCopy.setText(_translate("Dialog", "Copy to clipboard"))
        self.cbAlways.setText(_translate("Dialog", "Always on top"))
        self.btnMakeComment.setText(_translate("Dialog", "Make comment"))
        self.btnCopy.setText(_translate("Dialog", "Copy"))
        self.gbLang.setTitle(_translate("Dialog", "Language"))
        self.rbPython.setText(_translate("Dialog", "Python"))
        self.rbC.setText(_translate("Dialog", "C"))
        self.rbMatlab.setText(_translate("Dialog", "Matlab"))