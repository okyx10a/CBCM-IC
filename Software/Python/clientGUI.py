# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 848)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.overall_layout = QtWidgets.QVBoxLayout()
        self.overall_layout.setContentsMargins(5, 5, 5, 5)
        self.overall_layout.setSpacing(5)
        self.overall_layout.setObjectName("overall_layout")
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.setContentsMargins(5, 5, 5, 5)
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName("title_layout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title.setObjectName("title")
        self.title_layout.addWidget(self.title)
        self.authors = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authors.sizePolicy().hasHeightForWidth())
        self.authors.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authors.setFont(font)
        self.authors.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.authors.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.authors.setObjectName("authors")
        self.title_layout.addWidget(self.authors)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setPixmap(QtGui.QPixmap("rsz_3lassonde_300.jpg"))
        self.logo.setObjectName("logo")
        self.title_layout.addWidget(self.logo)
        self.overall_layout.addLayout(self.title_layout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.general_parameters = QtWidgets.QWidget()
        self.general_parameters.setObjectName("general_parameters")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.general_parameters)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gen_param_layout = QtWidgets.QVBoxLayout()
        self.gen_param_layout.setContentsMargins(5, 5, 5, 5)
        self.gen_param_layout.setSpacing(5)
        self.gen_param_layout.setObjectName("gen_param_layout")
        self.num_samp_hint = QtWidgets.QLabel(self.general_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_samp_hint.sizePolicy().hasHeightForWidth())
        self.num_samp_hint.setSizePolicy(sizePolicy)
        self.num_samp_hint.setObjectName("num_samp_hint")
        self.gen_param_layout.addWidget(self.num_samp_hint)
        self.num_samp = QtWidgets.QLineEdit(self.general_parameters)
        self.num_samp.setObjectName("num_samp")
        self.gen_param_layout.addWidget(self.num_samp)
        self.res_CCO_hint = QtWidgets.QLabel(self.general_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_CCO_hint.sizePolicy().hasHeightForWidth())
        self.res_CCO_hint.setSizePolicy(sizePolicy)
        self.res_CCO_hint.setObjectName("res_CCO_hint")
        self.gen_param_layout.addWidget(self.res_CCO_hint)
        self.res_CCO = QtWidgets.QLineEdit(self.general_parameters)
        self.res_CCO.setObjectName("res_CCO")
        self.gen_param_layout.addWidget(self.res_CCO)
        self.set_param = QtWidgets.QPushButton(self.general_parameters)
        self.set_param.setObjectName("set_param")
        self.gen_param_layout.addWidget(self.set_param)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gen_param_layout.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.gen_param_layout)
        self.tabWidget.addTab(self.general_parameters, "")
        self.set_cal = QtWidgets.QWidget()
        self.set_cal.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.set_cal.setObjectName("set_cal")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.set_cal)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.set_cal_layout = QtWidgets.QVBoxLayout()
        self.set_cal_layout.setContentsMargins(5, 5, 5, 5)
        self.set_cal_layout.setSpacing(5)
        self.set_cal_layout.setObjectName("set_cal_layout")
        self.cal_input_hint = QtWidgets.QLabel(self.set_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_input_hint.sizePolicy().hasHeightForWidth())
        self.cal_input_hint.setSizePolicy(sizePolicy)
        self.cal_input_hint.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cal_input_hint.setObjectName("cal_input_hint")
        self.set_cal_layout.addWidget(self.cal_input_hint)
        self.cal_input = QtWidgets.QLineEdit(self.set_cal)
        self.cal_input.setObjectName("cal_input")
        self.set_cal_layout.addWidget(self.cal_input)
        self.set_cal_2 = QtWidgets.QPushButton(self.set_cal)
        self.set_cal_2.setObjectName("set_cal_2")
        self.set_cal_layout.addWidget(self.set_cal_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.set_cal_layout.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.set_cal_layout)
        self.tabWidget.addTab(self.set_cal, "")
        self.scan_cal = QtWidgets.QWidget()
        self.scan_cal.setObjectName("scan_cal")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scan_cal)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scan_cal_layout = QtWidgets.QVBoxLayout()
        self.scan_cal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scan_cal_layout.setContentsMargins(5, 5, 5, 5)
        self.scan_cal_layout.setSpacing(5)
        self.scan_cal_layout.setObjectName("scan_cal_layout")
        self.start_scan = QtWidgets.QPushButton(self.scan_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_scan.sizePolicy().hasHeightForWidth())
        self.start_scan.setSizePolicy(sizePolicy)
        self.start_scan.setObjectName("start_scan")
        self.scan_cal_layout.addWidget(self.start_scan)
        self.Graphwindow = QtWidgets.QWidget(self.scan_cal)
        self.Graphwindow.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graphwindow.sizePolicy().hasHeightForWidth())
        self.Graphwindow.setSizePolicy(sizePolicy)
        self.Graphwindow.setObjectName("Graphwindow")
        self.scan_cal_layout.addWidget(self.Graphwindow)
        self.verticalLayout_9.addLayout(self.scan_cal_layout)
        self.tabWidget.addTab(self.scan_cal, "")
        self.overall_layout.addWidget(self.tabWidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName("textBrowser")
        self.overall_layout.addWidget(self.textBrowser)
        self.verticalLayout_3.addLayout(self.overall_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "CBCM IC"))
        self.authors.setText(_translate("MainWindow", "BioSA, E.Ghafar-Zadeh, K.Qiao"))
        self.num_samp_hint.setText(_translate("MainWindow", "Number of samples"))
        self.res_CCO_hint.setText(_translate("MainWindow", "CCO resulution"))
        self.set_param.setText(_translate("MainWindow", "Set parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_parameters), _translate("MainWindow", "General parameters"))
        self.cal_input_hint.setText(_translate("MainWindow", "Please enter calibration sequence in binary"))
        self.set_cal_2.setText(_translate("MainWindow", "Set calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_cal), _translate("MainWindow", "Set calibration"))
        self.start_scan.setText(_translate("MainWindow", "Start Scanning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_cal), _translate("MainWindow", "Scan calibration "))
