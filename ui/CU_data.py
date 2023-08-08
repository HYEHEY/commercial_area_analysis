from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class DataPage(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('./ui_file/CU_data.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(590, 241)
        self.back_btn.clicked.connect(lambda x:self.close())