from PyQt5.QtWidgets import QDialog, QLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd

class DataPage(QDialog):
    def __init__(self):
        super().__init__()
        # 기본 한글 폰트 설정
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
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
        plt.plot(df1['x'], df1['y'], color='blue', linestyle='-',marker='o')

        plt.xlim(2017, 2023)
        # plt.ylim(150000, 400000)
        plt.xlabel('년도')
        plt.ylabel('관광객 수(명)')
        plt.title("유동인구 그래프")
        plt.xticks(range(2018, 2023))

    def create_donut_chart(self):
        sizes = [10, 6, 8, 4, 7]  # 투두리스트 갯수가 들어가야 함.
        labels = ['A', 'B', 'C', 'D', 'E']  # 이름이 들어가야 함
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
        colors_ = ['#0F9B58', '#0FBC74', '#53B83A', '#3EC56B', '#1AA867', '#0FAF52', '#0FAF6B', '#53AF37']

        # 파이 차트 생성 (도넛 모양 속성을 가진)
        plt.pie(sizes, labels=labels, colors=colors_, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))

        # 도넛 모양으로 그래프 그리기
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # 동일한 비율로 그래프 그리기
        plt.axis('equal')
        plt.tight_layout()

    def show_population(self):
        """유동인구 출력 함수"""
        # 맷플롯 캔버스 만들기 및 레이아웃에 캔버스 추가
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)

        self.create_example_plot() # 막대 선그래프

    def show_infra(self):
        """주변 인프라 출력 함수"""
        self.clear_layout(self.verticalLayout)
        canvas = FigureCanvas(plt.figure())
        self.verticalLayout.addWidget(canvas)

        # 샘플 차트 생성
        self.create_donut_chart()  # 도넛 모양 그래프

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


