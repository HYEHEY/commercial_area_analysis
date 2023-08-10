import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

from CU_main import MainPage
from Code.class_client import ClientApp


class StartPage(QWidget):
    def __init__(self, client_app=ClientApp):
        isinstance(client_app, ClientApp)
        super().__init__()
        loadUi('./ui_file/CU_start.ui', self)
        self.client_app = client_app
        self.window_option()
        self.btn_event()

    def window_option(self):
        """프로그램 실행시 첫 화면 옵션 설정 함수"""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

    def btn_event(self):
        """버튼 클릭 이벤트 함수"""
        self.start_btn.clicked.connect(self.go_main_page)

    def go_main_page(self):
        """메인 페이지 이동 함수"""
        self.main = MainPage(self.client_app)
        self.close()
        self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_app = ClientApp()
    myWindow = StartPage(client_app)
    myWindow.show()
    app.exec_()