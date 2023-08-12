import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class StoreData(QWidget):
    def __init__(self, data_, parent=None):
        super().__init__(parent)
        loadUi('./ui_file/CU_store_item.ui', self)
        self.label_8.setText(f'1.주변 편의점 수 : {data_[0]} 개')
        self.label_9.setText(f'2.주변 편의점 평균 매출 : {data_[1]} 만원')
        self.label_10.setText(f'3.주변 편의점 평균 매출 건수 : {data_[2]} 건')
