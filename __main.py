# -*- coding: utf-8 -*-
 
import os
import sys
import copy
import math
from PySide.QtCore import Slot
from PySide.QtGui import *
from PySide.QtCore import *
from PIL import Image
from itertools import islice, takewhile
from scapy import Ui_MainWindow

class ScapyManiuplator(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(ScapyManiuplator, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()

    def assignWidgets(self):
        self.button_create_packet.clicked.connect(self.goPushed)
        self.button_delete_packet.clicked.connect(self.delPack)

    def goPushed(self):
        self.textBrowser.append("Tutaj dodaje tekst")

    def delPack(self):
        self.textBrowser.append("Skasowano pakiet")

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = ScapyManiuplator()
    ret = app.exec_()
    sys.exit(ret)