import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('./ui_file/CU_main.ui', self)
        self.window_option()
        self.btn_event()

    def window_option(self):
        """프로그램 실행시 첫 화면 옵션 설정 함수"""
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.pushButton_2.setChecked(True)
        self.title_lbl.setText("서울 관광지")
        self.comboBox.addItem("현대백화점 압구정본점")
        self.comboBox.addItem("신세계백화점 강남점")
        self.comboBox.addItem("타임스퀘어")
        self.comboBox.addItem("코엑스")
        self.comboBox.addItem("롯데몰 김포공항점")

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        region_btn_list = [self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8,
                           self.btn_9,self.btn_10,self.btn_11,self.btn_12,self.btn_13,self.btn_14,self.btn_15,
                           self.btn_16,self.btn_17]
        for idx, btn in enumerate(region_btn_list):
            btn.clicked.connect(lambda x=None, y=idx: self.region_info(y))

    def region_info(self, idx):
        """지역 정보 변경 이벤트 함수"""
        if idx == 0:
            self.comboBox.clear()
            self.title_lbl.setText("서울 관광지")
            self.comboBox.addItem("현대백화점 압구정본점")
            self.comboBox.addItem("신세계백화점 강남점")
            self.comboBox.addItem("타임스퀘어")
            self.comboBox.addItem("코엑스")
            self.comboBox.addItem("롯데몰 김포공항점")
        elif idx == 1:
            self.comboBox.clear()
            self.title_lbl.setText("경기 관광지")
            self.comboBox.addItem("스타필드 하남점")
            self.comboBox.addItem("스타필드 고양점")
            self.comboBox.addItem("현대백화점 판교점")
            self.comboBox.addItem("애버랜드")
            self.comboBox.addItem("현대프리미엄아울렛 김포점")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainPage()
    myWindow.show()
    app.exec_()
