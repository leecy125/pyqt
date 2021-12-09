#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: RunMainWindow.py
@time: 2021/12/9 17:00
@desc: 
"""
import sys

from PyQt5.QtCore import pyqtSlot

import demo1

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class Calc(QDialog, demo1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_0.clicked.connect(lambda x: self.button_click('0'))
        self.pushButton_1.clicked.connect(lambda x: self.button_click('1'))
        self.pushButton_2.clicked.connect(lambda x: self.button_click('2'))
        self.pushButton_3.clicked.connect(lambda x: self.button_click('3'))
        self.pushButton_4.clicked.connect(lambda x: self.button_click('4'))
        self.pushButton_5.clicked.connect(lambda x: self.button_click('5'))
        self.pushButton_6.clicked.connect(lambda x: self.button_click('6'))
        self.pushButton_7.clicked.connect(lambda x: self.button_click('7'))
        self.pushButton_8.clicked.connect(lambda x: self.button_click('8'))
        self.pushButton_8.clicked.connect(lambda x: self.button_click('9'))
        self.pushButton_clear.clicked.connect(lambda x: self.button_click('C'))
        self.pushButton_jia.clicked.connect(lambda x: self.button_click('+'))
        self.pushButton_jian.clicked.connect(lambda x: self.button_click('-'))
        self.pushButton_cheng.clicked.connect(lambda x: self.button_click('*'))
        self.pushButton_chu.clicked.connect(lambda x: self.button_click('/'))
        self.pushButton_equal.clicked.connect(lambda x: self.button_click('='))

        self.method = ''
        self.result = False
        self.first_num = ''
        self.second_num = ''

    def button_click(self, st):
        if self.method != '':
            self.second_num = st
            self.lineEdit.setText(str(eval(self.first_num + self.method + self.second_num)))
            self.first_num = self.lineEdit.text()
            self.second_num = ''
            self.method = ''
        elif st in ['+', '-', '*', '/']:
            self.method = st
            self.lineEdit.setText(self.first_num + self.method)
        elif st == '=':
            text = eval(self.lineEdit.text())
            self.lineEdit.setText(text)
        elif st == 'C':
            self.lineEdit.setText('0')
        else:
            self.first_num = st
            self.lineEdit.setText(self.first_num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    sys.exit(app.exec_())
