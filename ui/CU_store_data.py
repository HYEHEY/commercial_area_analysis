import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class StoreData(QWidget):
    def __init__(self, data_, num, parent=None):
        super().__init__(parent)
        loadUi('./ui_file/CU_store_item.ui', self)
        if num == 1:
            self.label_11.hide()
            self.label_13.hide()
            self.label_14.hide()
            self.label_3.setText("주변 편의점 데이터")
            self.label_8.setText(f'1.주변 편의점 수 : {data_[0]} 개')
            self.label_9.setText(f'2.주변 편의점 월 평균 매출 : {data_[1]} 만원')
            self.label_10.setText(f'3.주변 편의점 월 평균 매출 건수 : {data_[2]} 건')
        elif num == 2:
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.hide()
            self.label_7.hide()
            self.label_8.hide()
            self.label_9.hide()
            self.label_10.hide()
            self.label_3.setText("결과 및 예상 투자 비용")
            self.label_13.setText(f'예상 투자 비용: {data_[1]} 만원 ~ {data_[2]} 만원 + 인테리어 비용')
            if data_[0] >= 75:
                self.label_14.setText("이곳의 등급은 '상' 이므로 입지 추천합니다.")
            if 75 > data_[0] >= 50:
                self.label_14.setText("이곳의 등급은 '중' 이므로 입지 고려해보세요.")
            else:
                self.label_14.setText("이곳의 등급은 '하' 이므로 입지 비추천합니다.")