import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpacerItem, QSizePolicy
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal

from Code.class_client import ClientApp
from ui.CU_data import DataPage
from ui.CU_forsale_list import ForSaleList
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from Code.class_json import *


class MainPage(QWidget):
    tourist_name_signal = pyqtSignal(str)
    realty_info_signal = pyqtSignal(str)
    realty_data_signal = pyqtSignal(str)

    def __init__(self, clientapp):
        super().__init__()
        loadUi('./ui_file/CU_main.ui', self)

        self.window_option()
        self.clientapp = clientapp
        self.clientapp.set_widget(self)
        self.btn_event()
        self.lbl_event()
        self.kakao_map()
        self.signal_event()
        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()


    def kakao_map(self):
        """카카오 맵 API 출력 이벤트 함수"""
        self.webEngineView = QWebEngineView()
        self.webEngineView.load(QUrl("http://localhost/kmap/kakaomap.html"))
        self.verticalLayout_2.addWidget(self.webEngineView)

    def lbl_event(self):
        """라벨 클릭 이벤트 함수"""
        self.label_3.mousePressEvent = lambda x: self.close_event(None)

    def signal_event(self):
        """시그널 이벤트 함수"""
        self.tourist_name_signal.connect(self.map_move_event)
        self.realty_info_signal.connect(self.add_forsale_list)
        self.realty_data_signal.connect(self.go_data_page)

    def close_event(self, e):
        """프로그램 종료 함수"""
        self.close()

    def window_option(self):
        """프로그램 실행시 첫 화면 옵션 설정 함수"""
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btn_1.setChecked(True)
        self.set_text("서울", "현대백화점압구정본점", "신세계백화점강남점", "타임스퀘어", "코엑스", "롯데몰김포공항점")

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        region_btn_list = [self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8,
                           self.btn_9,self.btn_10,self.btn_11,self.btn_12,self.btn_13,self.btn_14,self.btn_15,
                           self.btn_16,self.btn_17]
        for idx, btn in enumerate(region_btn_list):
            btn.clicked.connect(lambda x=None, y=idx: self.region_info(y))
        self.search_btn.clicked.connect(self.map_search)

    def set_text(self, region, t1, t2, t3, t4, t5):
        """지역 정보 텍스트 변경 이벤트 함수"""
        self.comboBox.clear()
        self.title_lbl.setText(f"{region} 관광지 내 입지 추천")
        self.comboBox.addItem(" ----------------------")
        self.comboBox.addItem(f"{t1}")
        self.comboBox.addItem(f"{t2}")
        self.comboBox.addItem(f"{t3}")
        self.comboBox.addItem(f"{t4}")
        self.comboBox.addItem(f"{t5}")

    def region_info(self, idx):
        """지역 정보 함수"""
        if idx == 0:
            self.set_text("서울", "현대백화점압구정본점", "신세계백화점강남점", "타임스퀘어", "코엑스", "롯데몰김포공항점")
        elif idx == 1:
            self.set_text("경기", "스타필드하남", "스타필드고양", "현대백화점판교점", "애버랜드", "현대프리미엄아울렛김포점")
        elif idx == 2:
            self.set_text("인천", "현대프리미엄아울렛송도점", "롯데백화점인천점", "소래포구종합어시장", "인천종합어시장", "소래포구")
        elif idx == 3:
            self.set_text("세종", "세종호수공원", "CGV세종", "세종전통시장", "금강보행교", "메가박스세종나성")
        elif idx == 4:
            self.set_text("대전", "갤러리아백화점타임월드점", "롯데백화점대전점", "현대프리미엄아울렛대전점", "오정농수산물도매시장",
                          "대전월드컵경기장")
        elif idx == 5:
            self.set_text("대구", "신세계백화점대구점", "서문시장", "현대백화점대구점", "수성못", "EXCO서관")
        elif idx == 6:
            self.set_text("부산", "신세계백화점센텀시티점", "롯데백화점부산본점", "롯데프리미엄아울렛동부산점",
                          "해운대해수욕장", "광안리해수욕장")
        elif idx == 7:
            self.set_text("울산", "현대백화점울산점", "롯데백화점울산점", "진하해수욕장", "일산해수욕장", "태화강국가정원")
        elif idx == 8:
            self.set_text("광주", "신세계백화점광주점", "롯데백화점광주점", "김대중컨벤션센터", "메가박스광주하남",
                          "롯데아울렛광주수완점")
        elif idx == 9:
            self.set_text("강원", "속초관광수산시장", "속초해수욕장", "안목해변", "강릉중앙시장", "주문진항")
        elif idx == 10:
            self.set_text("경남", "롯데백화점창원점", "창원컨벤션센터", "독일마을", "통도사", "진주중앙시장")
        elif idx == 11:
            self.set_text("경북", "죽도시장", "첨성대", "영일대해수욕장", "롯데백화점포항점", "보문관광단지")
        elif idx == 12:
            self.set_text("전남", "이순신광장", "죽녹원", "오동도", "향일암", "여수해상케이블카놀아정류장")
        elif idx == 13:
            self.set_text("전북", "전주한옥마을", "롯데몰군산점", "전주월드컵경기장", "롯데백화점전주점", "전주동물원")
        elif idx == 14:
            self.set_text("충남", "삽교호관광지", "신세계백화점천안아산점", "독립기념관", "예당호출렁다리", "갤러리아백화점센터시티점")
        elif idx == 15:
            self.set_text("충북", "현대백화점충청점", "오창호수공원", "단양구경시장", "청풍호반케이블카", "롯데아울렛청주점")
        elif idx == 16:
            self.set_text("제주", "동문재래시장", "서귀포매일올레시장", "성산일출봉", "함덕해수욕장", "곽지해수욕장")

    def go_data_page(self, data_):
        """데이터 페이지 출력 함수"""
        data = DataPage(self.clientapp, data_)
        data.exec_()

    def add_forsale_list(self, info):
        """매물 리스트 add widget 함수"""
        self.clear_forsale_list()
        information = self.decoder.binary_to_obj(info)
        for info_ in information:
            for_sale = ForSaleList(info_)
            for_sale.setParent(self.scrollAreaWidgetContents)
            self.scrollArea.widget().layout().insertWidget(len(self.scrollArea.widget().layout()) - 1, for_sale)
            for_sale.mousePressEvent = lambda x=None, y=info_: self.go_data_page(y)

    def clear_forsale_list(self):
        """매물 리스트 클리어 이벤트 함수"""
        layout = self.verticalLayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
        self.Spacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(self.Spacer)

    def map_search(self):
        """카카오 맵 검색 이벤트 함수"""
        tourist_name = self.comboBox.currentText()
        if tourist_name == " ----------------------":
            return
        else:
            self.clientapp.send_tourist_name_access(tourist_name)

    def map_move_event(self, info):
        """콤보박스 검색 값 map_move 함수에 좌표 넘겨주는 함수"""
        information = self.decoder.binary_to_obj(info)[0]
        x_value = information.tou_x
        y_value = information.tou_y
        self.map_move(x_value, y_value)

    def map_move(self, x, y):
        """카카오 맵 좌표 값에 따라 이동 이벤트 함수"""
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", x, y)
        page = page.runJavaScript(script)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clientapp = ClientApp()
    myWindow = MainPage(clientapp)
    myWindow.show()
    app.exec_()
