import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

from ui.CU_data import DataPage


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
        self.set_text("서울", "현대백화점 압구정본점", "신세계백화점 강남점", "타임스퀘어", "코엑스", "롯데몰 김포공항점")

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        region_btn_list = [self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8,
                           self.btn_9,self.btn_10,self.btn_11,self.btn_12,self.btn_13,self.btn_14,self.btn_15,
                           self.btn_16,self.btn_17]
        for idx, btn in enumerate(region_btn_list):
            btn.clicked.connect(lambda x=None, y=idx: self.region_info(y))
        self.search_btn.clicked.connect(self.go_data_page)

    def set_text(self, region, t1, t2, t3, t4, t5):
        """지역 정보 텍스트 변경 이벤트 함수"""
        self.comboBox.clear()
        self.title_lbl.setText(f"{region} 관광지 내 입지 추천")
        self.comboBox.addItem("전체")
        self.comboBox.addItem(f"{t1}")
        self.comboBox.addItem(f"{t2}")
        self.comboBox.addItem(f"{t3}")
        self.comboBox.addItem(f"{t4}")
        self.comboBox.addItem(f"{t5}")

    def region_info(self, idx):
        """지역 정보 함수"""
        if idx == 0:
            self.set_text("서울", "현대백화점 압구정본점", "신세계백화점 강남점", "타임스퀘어", "코엑스", "롯데몰 김포공항점")
        elif idx == 1:
            self.set_text("경기", "스타필드 하남점", "스타필드 고양점", "현대백화점 판교점", "애버랜드", "현대프리미엄아울렛 김포점")
        elif idx == 2:
            self.set_text("인천", "현대프로미엄아울렛 송도점", "롯데백화점 인천점", "소래포구 종합어시장", "인천 종합어시장", "소래포구")
        elif idx == 3:
            self.set_text("세종", "세종 호수공원", "CGV 세종점", "세종 전통시장", "금강보행교", "메가박스 세종나성점")
        elif idx == 4:
            self.set_text("대전", "갤러리아백화점 타임월드점", "롯데백화점 대전점", "현대프리미엄아울렛 대전점", "오정농수산물 도매시장",
                          "대전 월드컵경기장")
        elif idx == 5:
            self.set_text("대구", "신세계백화점 대구점", "서문시장", "현대백화점 대구점", "수성못", "EXCO서관")
        elif idx == 6:
            self.set_text("부산", "신세계백화점 센텀시티점", "롯데백화점 부산본점", "롯데프리미엄아울렛 동부산점",
                          "해운대 해수욕장", "광안리 해수욕장")
        elif idx == 7:
            self.set_text("울산", "현대백화점 울산점", "진하 해수욕장", "일산 해수욕장", "태화강 국가정원", "업스퀘어")
        elif idx == 8:
            self.set_text("광주", "신세계백화점 광주점", "롯데백화점 광주점", "김대중 컨벤션센터", "메가박스 광주하남점",
                          "롯데아울렛 광주수완점")
        elif idx == 9:
            self.set_text("강원", "속초 관광수산시장", "속초 해수욕장", "안목해변", "강릉 중앙시장", "주문진항")
        elif idx == 10:
            self.set_text("경남", "롯데백화점 창원점", "창원 컨벤션센터", "독일마을", "통도사", "진주 중앙시장")
        elif idx == 11:
            self.set_text("경북", "죽도시장", "첨성대", "영일대 해수욕장", "롯데백화점 포항점", "보문관광단지")
        elif idx == 12:
            self.set_text("전남", "이순신 광장", "죽녹원", "오동도", "항일암", "여수 해상케이블카 놀아정류장")
        elif idx == 13:
            self.set_text("전북", "전주 한옥마을", "롯데몰 군산점", "전주 월드컵경기장", "롯데백화점 전주점", "전주 동물원")
        elif idx == 14:
            self.set_text("충남", "삽교호 관광지", "신세계백화점 천안아산점", "독립기념관", "예당호 출렁다리", "갤러리아백화점 센터시티점")
        elif idx == 15:
            self.set_text("충북", "현대백화점 충청점", "오창 호수공원", "단양 구경시장", "청풍호반 케이블카", "롯데아울렛 청주점")
        elif idx == 16:
            self.set_text("제주", "동문재래시장", "서귀포 매일 올레시장", "성산일출봉", "함덕 해수욕장", "곽지 해수욕장")

    def go_data_page(self):
        """데이터 페이지 출력 함수"""
        data = DataPage()
        data.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainPage()
    myWindow.show()
    app.exec_()
