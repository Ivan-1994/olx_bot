from bot_olx import olx_serch
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QGridLayout, QApplication, QPushButton, QListWidget)
from db_dict import categories, region_ua

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.choice_categories = []
        self.choice_region = []
        btn1 = QPushButton("Старт", self)
        title = QLabel('Сообщение поиска: ')
        self.titleEdit = QLineEdit('')
        # Блок Регион
        self.list_region_Widget = QListWidget()
        self.list_region_Widget.show()
        self.list_region_Widget.addItems(region_ua)
        # Блок город
        self.list_sub_region_Widget = QListWidget()
        self.list_sub_region_Widget.show()
        # Блок категории
        self.list_category_Widget = QListWidget()
        self.list_category_Widget.show()
        self.list_category_Widget.addItems(categories)
        # Блок подкатегории
        self.list_sub_category_Widget = QListWidget()
        self.list_sub_category_Widget.show()

        grid = QGridLayout()
        grid.setSpacing(20)
        # Название поля
        grid.addWidget(title, 0, 0)
        # Поле поиска
        grid.addWidget(self.titleEdit, 0, 1, 1, 3)
        # Кнопка
        grid.addWidget(btn1, 2, 0, 1, 4)
        # Категории
        grid.addWidget(self.list_category_Widget, 3, 0)
        grid.addWidget(self.list_sub_category_Widget, 3, 1)
        # Регионы
        grid.addWidget(self.list_region_Widget, 3, 2)
        grid.addWidget(self.list_sub_region_Widget, 3, 3)
        self.setLayout(grid)

        self.setGeometry(250, 250, 1100, 900)
        self.setWindowTitle('Olx парсер номеров')



        self.list_region_Widget.clicked.connect(self.event_list_region)
        self.list_sub_region_Widget.clicked.connect(self.choice_list_sub_region)

        self.list_category_Widget.clicked.connect(self.event_list_me)
        self.list_sub_category_Widget.clicked.connect(self.choice_list_me)

        btn1.clicked.connect(self.buttonClicked)
        self.show()

    # По регионам
    def event_list_region(self):
        selected = [item.text() for item in self.list_region_Widget.selectedItems()]
        self.list_sub_region_Widget.clear()
        self.list_sub_region_Widget.addItems(region_ua[selected[0]][1])
        
    def choice_list_sub_region(self):
        selected = [item.text() for item in self.list_region_Widget.selectedItems()]
        sub_selected = [item.text() for item in self.list_sub_region_Widget.selectedItems()]
        self.choice_region.clear()
        self.choice_region.append(region_ua[selected[0]][0])
        self.choice_region.append(region_ua[selected[0]][1][sub_selected[0]])

    # По категориям
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
        olx_serch(self.titleEdit.text(), self.choice_categories, self.choice_region)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())