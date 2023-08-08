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
        self.btn_1.setChecked(True)
        self.title_lbl.setText("서울 관광지 내 입지 추천")
        self.comboBox.addItem("전체")
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
            self.title_lbl.setText("서울 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("현대백화점 압구정본점")
            self.comboBox.addItem("신세계백화점 강남점")
            self.comboBox.addItem("타임스퀘어")
            self.comboBox.addItem("코엑스")
            self.comboBox.addItem("롯데몰 김포공항점")
        elif idx == 1:
            self.comboBox.clear()
            self.title_lbl.setText("경기 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("스타필드 하남점")
            self.comboBox.addItem("스타필드 고양점")
            self.comboBox.addItem("현대백화점 판교점")
            self.comboBox.addItem("애버랜드")
            self.comboBox.addItem("현대프리미엄아울렛 김포점")
        elif idx == 2:
            self.comboBox.clear()
            self.title_lbl.setText("인천 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("현대프리미엄아울렛 송도점")
            self.comboBox.addItem("롯데백화점 인천점")
            self.comboBox.addItem("소래포구 종합어시장")
            self.comboBox.addItem("인천 종합어시장")
            self.comboBox.addItem("소래포구")
        elif idx == 3:
            self.comboBox.clear()
            self.title_lbl.setText("세종 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("세종 호수공원")
            self.comboBox.addItem("CGV 세종점")
            self.comboBox.addItem("세종 전통시장")
            self.comboBox.addItem("금강보행교")
            self.comboBox.addItem("메가박스 세종나성점")
        elif idx == 4:
            self.comboBox.clear()
            self.title_lbl.setText("대전 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("갤러리아백화점 타임월드점")
            self.comboBox.addItem("롯데백화점 대전점")
            self.comboBox.addItem("현대프리미엄아울렛 대전점")
            self.comboBox.addItem("오정농수산물 도매시장")
            self.comboBox.addItem("대전 월드컵경기장")
        elif idx == 5:
            self.comboBox.clear()
            self.title_lbl.setText("대구 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("신세계백화점 대구점")
            self.comboBox.addItem("서문시장")
            self.comboBox.addItem("현대백화점 대구점")
            self.comboBox.addItem("수성못")
            self.comboBox.addItem("EXCO서관")
        elif idx == 6:
            self.comboBox.clear()
            self.title_lbl.setText("부산 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("신세계백화점 센텀시티점")
            self.comboBox.addItem("롯데백화점 부산본점")
            self.comboBox.addItem("롯데프리미엄아울렛 동부산점")
            self.comboBox.addItem("해운대 해수욕장")
            self.comboBox.addItem("광안리 해수욕장")
        elif idx == 7:
            self.comboBox.clear()
            self.title_lbl.setText("울산 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("현대백화점 울산점")
            self.comboBox.addItem("진하 해수욕장")
            self.comboBox.addItem("일산 해수욕장")
            self.comboBox.addItem("태화강 국가정원")
            self.comboBox.addItem("업스퀘어")
        elif idx == 8:
            self.comboBox.clear()
            self.title_lbl.setText("광주 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("신세계백화점 광주점")
            self.comboBox.addItem("롯데백화점 광주점")
            self.comboBox.addItem("김대중 컨벤션센터")
            self.comboBox.addItem("메가박스 광주하남점")
            self.comboBox.addItem("롯데아울렛 광주수완점")
        elif idx == 9:
            self.comboBox.clear()
            self.title_lbl.setText("강원 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("속초 관광수산시장")
            self.comboBox.addItem("속초 해수욕장")
            self.comboBox.addItem("안목해변")
            self.comboBox.addItem("강릉 중앙시장")
            self.comboBox.addItem("주문진항")
        elif idx == 10:
            self.comboBox.clear()
            self.title_lbl.setText("경남 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("롯데백화점 창원점")
            self.comboBox.addItem("창원 컨벤션센터")
            self.comboBox.addItem("독일마을")
            self.comboBox.addItem("통도사")
            self.comboBox.addItem("진주 중앙시장")
        elif idx == 11:
            self.comboBox.clear()
            self.title_lbl.setText("경북 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("죽도시장")
            self.comboBox.addItem("첨성대")
            self.comboBox.addItem("영일대 해수욕장")
            self.comboBox.addItem("롯데백화점 포항점")
            self.comboBox.addItem("보문관광단지")
        elif idx == 12:
            self.comboBox.clear()
            self.title_lbl.setText("전남 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("이순신 광장")
            self.comboBox.addItem("죽녹원")
            self.comboBox.addItem("오동도")
            self.comboBox.addItem("항일암")
            self.comboBox.addItem("여수 해상케이블카 놀아정류장")
        elif idx == 13:
            self.comboBox.clear()
            self.title_lbl.setText("전북 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("전주 한옥마을")
            self.comboBox.addItem("롯데몰 군산점")
            self.comboBox.addItem("전주 월드컵경기장")
            self.comboBox.addItem("롯데백화점 전주점")
            self.comboBox.addItem("전주 동물원")
        elif idx == 14:
            self.comboBox.clear()
            self.title_lbl.setText("충남 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("삽교호 관광지")
            self.comboBox.addItem("신세계백화점 천안아산점")
            self.comboBox.addItem("독립기념관")
            self.comboBox.addItem("예당호 출렁다리")
            self.comboBox.addItem("코스트코홀세일 천안점")
        elif idx == 15:
            self.comboBox.clear()
            self.title_lbl.setText("충북 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("현대백화점 충청점")
            self.comboBox.addItem("오창 호수공원")
            self.comboBox.addItem("단양 구경시장")
            self.comboBox.addItem("청풍호반 케이블카")
            self.comboBox.addItem("롯데아울렛 청주점")
        elif idx == 16:
            self.comboBox.clear()
            self.title_lbl.setText("제주 관광지 내 입지 추천")
            self.comboBox.addItem("전체")
            self.comboBox.addItem("동문재래시장")
            self.comboBox.addItem("서귀포 매일 올레시장")
            self.comboBox.addItem("성산일출봉")
            self.comboBox.addItem("함덕 해수욕장")
            self.comboBox.addItem("곽지 해수욕장")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainPage()
    myWindow.show()
    app.exec_()
