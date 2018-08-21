from olx_bot.bot_olx import olx_serch
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QGridLayout, QApplication, QPushButton, QListWidget)
from olx_bot.db_dict import categories, region_ua

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.choice_categories = []
        btn1 = QPushButton("Старт", self)
        title = QLabel('Сообщение поиска: ')
        self.titleEdit = QLineEdit('')

        self.list_category_Widget = QListWidget()
        self.list_category_Widget.show()
        self.list_category_Widget.addItems(categories)

        self.list_sub_category_Widget = QListWidget()
        self.list_sub_category_Widget.show()

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(title, 0, 0)
        grid.addWidget(self.titleEdit, 1, 0)
        grid.addWidget(btn1, 2, 0)
        grid.addWidget(self.list_category_Widget, 3, 0)
        grid.addWidget(self.list_sub_category_Widget, 3, 1)
        self.setLayout(grid)

        self.setGeometry(250, 250, 600, 800)
        self.setWindowTitle('Olx парсер номеров')

        btn1.clicked.connect(self.buttonClicked)
        self.list_category_Widget.clicked.connect(self.event_list_me)
        self.list_sub_category_Widget.clicked.connect(self.choice_list_me)
        self.show()

    def event_list_me(self):
        selected = [item.text() for item in self.list_category_Widget.selectedItems()]
        self.list_sub_category_Widget.clear()
        self.list_sub_category_Widget.addItems(categories[selected[0]][1])

    def choice_list_me(self):
        selected = [item.text() for item in self.list_category_Widget.selectedItems()]
        sub_selected = [item.text() for item in self.list_sub_category_Widget.selectedItems()]
        self.choice_categories.clear()
        self.choice_categories.append(categories[selected[0]][0])
        self.choice_categories.append(categories[selected[0]][1][sub_selected[0]])

    def buttonClicked(self):
        olx_serch(self.titleEdit.text(), self.choice_categories)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())