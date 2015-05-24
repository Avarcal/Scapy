# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scapy.ui'
#
# Created: Fri May 22 15:40:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Scapy Manipulator")
        MainWindow.resize(743, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 231, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_create_packet = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_create_packet.setObjectName("button_create_packet")
        self.verticalLayout.addWidget(self.button_create_packet)
        self.button_delete_packet = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_delete_packet.setObjectName("button_delete_packet")
        self.verticalLayout.addWidget(self.button_delete_packet)
        self.button_send_packet = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_send_packet.setObjectName("button_send_packet")
        self.verticalLayout.addWidget(self.button_send_packet)
        self.button_sniff = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_sniff.setObjectName("button_sniff")
        self.verticalLayout.addWidget(self.button_sniff)
        self.button_rw_pcap = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_rw_pcap.setObjectName("button_rw_pcap")
        self.verticalLayout.addWidget(self.button_rw_pcap)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_fuzzing = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_fuzzing.setObjectName("button_fuzzing")
        self.verticalLayout.addWidget(self.pushButton_fuzzing)
        # Text Browser - Console
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 230, 411, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 90, 131, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 140, 181, 17))
        self.label_3.setObjectName("label_3")
        # Text Browser - Stworzone pakiety
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(470, 40, 191, 20))
        self.textBrowser_2.setObjectName("textBrowser_created")
        # Text Browser - Wysłane pakiety
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(470, 90, 191, 20))
        self.textBrowser_3.setObjectName("textBrowser_3")
        # Text Browser - Przechwycone pakiety
        self.textBrowser_4 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(470, 140, 191, 20))
        self.textBrowser_4.setObjectName("textBrowser_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("Scapy Manipulator", "Scapy Manipulator", None, QtGui.QApplication.UnicodeUTF8))
        self.button_create_packet.setText(QtGui.QApplication.translate("Scapy Manipulator", "Stwórz pakiet", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete_packet.setText(QtGui.QApplication.translate("Scapy Manipulator", "Usuń pakiet", None, QtGui.QApplication.UnicodeUTF8))
        self.button_send_packet.setText(QtGui.QApplication.translate("Scapy Manipulator", "Wyślij pakiety", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sniff.setText(QtGui.QApplication.translate("Scapy Manipulator", "Sniff", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rw_pcap.setText(QtGui.QApplication.translate("Scapy Manipulator", "R & W PCAP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Scapy Manipulator", "Stwórz grupę pakietów", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_fuzzing.setText(QtGui.QApplication.translate("Scapy Manipulator", "Fuzzing", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Scapy Manipulator", "Stworzone pakiety", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Scapy Manipulator", "Wysłane pakiety", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Scapy Manipulator", "Przechwycone pakiety", None, QtGui.QApplication.UnicodeUTF8))

