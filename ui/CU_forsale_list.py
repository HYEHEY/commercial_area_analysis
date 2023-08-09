import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class ForSaleList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('./ui_file/CU_list_item.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = ForSaleList()
    myWindow.show()
    app.exec_()