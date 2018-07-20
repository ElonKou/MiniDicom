#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: main.py 
@time: 18-5-31 下午6:33 
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MiniDicom')
        self.setWindowIcon(QIcon('./src/image/icon.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
