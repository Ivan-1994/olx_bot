#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bot_olx import olx_serch
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QGridLayout, QApplication, QPushButton, QTextBrowser)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1 = QPushButton("Старт", self)

        title = QLabel('Сообщение поиска: ')
        self.titleEdit = QLineEdit('')

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(title, 0, 1)
        grid.addWidget(self.titleEdit, 1, 1)
        grid.addWidget(btn1, 2, 1)
        self.setLayout(grid)

        self.setGeometry(250, 250, 600, 150)
        self.setWindowTitle('Olx парсер номеров')

        btn1.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        olx_serch(self.titleEdit.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())