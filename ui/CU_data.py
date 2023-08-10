from PyQt5.QtWidgets import QDialog, QLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm
import pandas as pd


class DataPage(QDialog):
    def __init__(self, id_):
        super().__init__()
        # 기본 한글 폰트 설정
        font_path = "C:\\Users\\KDT113\\AppData\\Local\\Microsoft\\Windows\\Fonts\\TmoneyRoundWindExtraBold.ttf"
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        loadUi('./ui_file/CU_data.ui', self)
        self.window_option()
        self.btn_event()

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        self.back_btn.clicked.connect(lambda x: self.close())
        self.back_btn_2.clicked.connect(self.show_population)
        self.back_btn_3.clicked.connect(self.show_infra)

    def create_example_plot(self):
        """꺾은선 그래프 출력 함수"""
        df1 = pd.DataFrame({'x':[2018, 2019, 2020, 2021, 2022], 'y':[204595, 261926, 332034, 319947, 255660]})
        plt.plot(df1['x'], df1['y'], color='blue', alpha=0.4, linestyle='-',marker='o')

        plt.xlim(2017, 2023)
        plt.xlabel('년도')
        plt.ylabel('관광객 수(명)')
        plt.title("유동인구 그래프")
        plt.xticks(range(2018, 2023))

    def create_plot(self):
        """막대 그래프 출력 함수"""
        list_x = [2019, 2020, 2021, 2022]
        list_y = [1, 2, 3, 4]

        plt.bar(list_x, list_y, color='blue', width=0.5, alpha=0.4)
        plt.xlabel('년도')
        plt.ylabel('개수')
        plt.title("막대 그래프")
        plt.xticks(range(2019, 2023))

    def show_population(self):
        """유동인구 출력 함수"""
        # 맷플롯 캔버스 만들기 및 레이아웃에 캔버스 추가
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)

        self.create_example_plot() # 선 그래프

    def show_infra(self):
        """주변 인프라 출력 함수"""
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)

        # 샘플 차트 생성
        self.create_plot()  # 막대 그래프

    def window_option(self):
        """프로그램 실행시 첫 화면 옵션 설정 함수"""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.move(590, 241)
        self.back_btn_2.setChecked(True)
        self.show_population()

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


