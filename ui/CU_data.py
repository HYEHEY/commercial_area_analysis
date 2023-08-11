from PyQt5.QtWidgets import QDialog, QLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm
import matplotlib.image as img
import pandas as pd
from Code.class_json import *


class DataPage(QDialog):
    year_data_signal = pyqtSignal(str)
    infra_data_signal = pyqtSignal(str)

    def __init__(self, clientapp, data_):
        super().__init__()
        # 기본 한글 폰트 설정
        font_path = "C:\\Users\\KDT113\\AppData\\Local\\Microsoft\\Windows\\Fonts\\TmoneyRoundWindExtraBold.ttf"
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        loadUi('./ui_file/CU_data.ui', self)
        self.clientapp = clientapp
        self.clientapp.set_widget(self)
        self.data = data_
        self.window_option()
        self.btn_event()
        self.signal_event()
        self.population_signal()
        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()

    def signal_event(self):
        """시그널 이벤트 함수"""
        self.year_data_signal.connect(self.show_population)
        self.infra_data_signal.connect(self.show_infra)

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        self.back_btn.clicked.connect(lambda x: self.close())
        self.back_btn_2.clicked.connect(self.population_signal)
        self.back_btn_3.clicked.connect(self.infra_signal)

    def create_population_plot(self, year_):
        """꺾은선 그래프 출력 함수"""
        year_data = self.decoder.binary_to_obj(year_)
        year_list = []
        year_personnel_list = []
        for year in year_data:
            year_id = year.yea_id
            years = year.yea_year
            year_list.append(years)
            year_tourist = year.yea_tourist
            year_personnel = year.yea_personnel
            year_personnel_list.append(year_personnel)

        df1 = pd.DataFrame({'x': year_list, 'y': year_personnel_list})
        plt.plot(df1['x'], df1['y'], color='blue', alpha=0.4, linestyle='-', marker='*')

        plt.xlim((year_list[0]-1), (year_list[-1]+1))
        plt.xlabel('년도')
        plt.ylabel('관광객 수(명)')
        plt.title("관광지 방문객 수")
        plt.xticks(range((year_list[0]), (year_list[-1]+1)))

    def create_infra_plot(self, infra_):
        """파이 그래프 출력 함수"""
        infra_data = self.decoder.binary_to_obj(infra_)
        infra_list = list()
        mart = infra_data.inf_mt1
        infra_list.append(mart)
        store = infra_data.inf_cs2
        infra_list.append(store)
        child = infra_data.inf_ps3
        infra_list.append(child)
        school = infra_data.inf_sc4
        infra_list.append(school)
        academy = infra_data.inf_ac5
        infra_list.append(academy)
        parking = infra_data.inf_pk6
        infra_list.append(parking)
        oil = infra_data.inf_ol7
        infra_list.append(oil)
        subway = infra_data.inf_sw8
        infra_list.append(subway)
        bank = infra_data.inf_bk9
        infra_list.append(bank)
        cultural = infra_data.inf_ct1
        infra_list.append(cultural)
        brokerage = infra_data.inf_ag2
        infra_list.append(brokerage)
        public = infra_data.inf_po3
        infra_list.append(public)
        attractions = infra_data.inf_at4
        infra_list.append(attractions)
        hotel = infra_data.inf_ad5
        infra_list.append(hotel)
        restaurant = infra_data.inf_fd6
        infra_list.append(restaurant)
        cafe = infra_data.inf_ce7
        infra_list.append(cafe)
        hospital = infra_data.inf_hp8
        infra_list.append(hospital)
        pharmacy = infra_data.inf_pm9
        infra_list.append(pharmacy)

        infra_num_list = list()
        labels = list()
        label = ['대형마트', '편의점', '어린이집,유치원', '학교', '학원', '주차장', '주유소', '지하철역',
                  '은행', '문화시설', '중개업소', '공공기관', '관광명소', '숙박', '음식점', '카페', '병원', '약국']
        for infra, label in zip (infra_list, label):
            if infra != 0:
                infra_num_list.append(infra)
                labels.append(label)
        ratio = infra_num_list
        colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#ffe4e1', '#faebd7', '#cbbeb5', '#f5f5dc', '#89a5ea',
                  '#ff8e7f', '#a5ea89', '#929292', '#ffcb6b', '#800000', '#59227c', '#6ccad0', '#99cc66', '#ccffff']
        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

        if len(infra_num_list) == 0:
            img_ = img.imread('./ui_img/텅.png')
            plt.imshow(img_)
            plt.rcParams["figure.figsize"] = (10,5)
            plt.gca().axes.xaxis.set_visible(False)
            plt.gca().axes.yaxis.set_visible(False)
            plt.axis('off')
        else:
            plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors,
                    wedgeprops=wedgeprops)
            plt.title("매물기준 반경 330m 주변 인프라", pad=30)
            plt.axis('equal')



    def population_signal(self):
        """클라이언트로 인구 데이터 시그널 전송 함수"""
        self.clientapp.send_realty_info_access(self.data)

    def infra_signal(self):
        """클라이언트로 인프라 데이터 시그널 전송 함수"""
        self.clientapp.send_infra_data_access(self.data)

    def show_population(self, year_):
        """유동인구 출력 함수"""
        # 맷플롯 캔버스 만들기 및 레이아웃에 캔버스 추가
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)
        self.create_population_plot(year_)

    def show_infra(self, infra_):
        """주변 인프라 출력 함수"""
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)

        # 샘플 차트 생성
        self.create_infra_plot(infra_)  # 파이 그래프

    def window_option(self):
        """프로그램 실행시 첫 화면 옵션 설정 함수"""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.move(590, 241)
        self.back_btn_2.setChecked(True)

    def clear_layout(self, layout: QLayout):
        """레이아웃 안의 모든 객체를 지웁니다."""
        if layout is None or not layout.count():
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.setParent(None)
            # 아이템이 레이아웃일 경우 재귀 호출로 레이아웃 내의 위젯 삭제
            else:
                self.clear_layout(item.layout())


