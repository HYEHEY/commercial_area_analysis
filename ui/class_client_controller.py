from PyQt5.QtCore import QPoint, Qt, pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow

from common.class_json import *

from CODE.class_client import ClientApp
from UI.widget_class_header import Header
from UI.ui.ui_class_main import Ui_MainWindow
from UI.widget_class_login_page import LoginWidget
from UI.widget_class_join_page import JoinWidget
from UI.widget_class_main_page import MainPageWidget
from UI.widget_class_search_page import SearchWidget
from UI.widget_class_big_book_info import BigBookInfo
from UI.widget_class_inquiry_chat_room import InquiryChatRoom
from UI.widget_class_book_info import BookInfo


class WindowController(QMainWindow, Ui_MainWindow):
    join_access_signal = pyqtSignal(bool)
    log_in_signal = pyqtSignal(bool)
    book_name_search_signal = pyqtSignal(str)
    book_writer_search_signal = pyqtSignal(str)
    book_publisher_search_signal = pyqtSignal(str)
    book_rental_signal = pyqtSignal(str)
    book_reservation_signal = pyqtSignal(str)

    def __init__(self, client_app=ClientApp):
        isinstance(client_app, ClientApp)
        super().__init__()
        self.client_app = client_app
        self.client_app.set_widget(self)
        self.widget_header = Header(self)
        self.widget_login_page = LoginWidget(self)
        self.widget_join_page = JoinWidget(self)
        self.widget_main_page = MainPageWidget(self)
        self.widget_search_page = SearchWidget(self)
        self.widget_inquiry_room = InquiryChatRoom(self)

        self.setupUi(self)
        self.page_3.setLayout(QVBoxLayout(self.page_3))
        self.page_4.setLayout(QVBoxLayout(self.page_4))
        self.page_5.setLayout(QVBoxLayout(self.page_5))
        self.valid_duplication_id = None
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.join_access_signal.connect(self.join_access_res)
        self.log_in_signal.connect(self.log_in_res)
        self.book_name_search_signal.connect(self.search_book)
        self.book_writer_search_signal.connect(self.search_book)
        self.book_publisher_search_signal.connect(self.search_book)
        self.book_rental_signal.connect(self.client_book_rental_res)
        self.book_reservation_signal.connect(self.client_book_reservation_res)

        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()

        self.set_login_widget()
        self.show()

    # 로그인 페이지 설정
    def set_login_widget(self):
        # 로그인 페이지 설정
        vbox_layout = QVBoxLayout(self)
        vbox_layout.addWidget(self.widget_login_page)
        self.page.setLayout(vbox_layout)
        self.stackedWidget.setCurrentIndex(0)

    # 로그인 정보 넘겨주기
    def log_in(self, login_id, login_pw):
        self.client_app.send_id_and_pw_login_access(login_id, login_pw)

    # 로그인 결과
    def log_in_res(self, return_result):
        if return_result:
            QtWidgets.QMessageBox.about(self, "성공", "로그인 완료")
            self.widget_login_page.라벨명.setText()
            # 메인페이지로
            self.set_main_page_widget()
        else:
            QtWidgets.QMessageBox.about(self, "실패", "로그인 실패")

    # 회원가입 페이지 설정
    def set_join_widget(self):
        vbox_layout = QVBoxLayout(self)
        vbox_layout.addWidget(self.widget_join_page)
        self.page_2.setLayout(vbox_layout)
        self.stackedWidget.setCurrentIndex(self.page_2)

    # 회원가입 페이지로
    def show_join_page(self):
        self.set_join_widget()
        self.stackedWidget.setCurrentWidget(self.page_2)

    # 회원가입 아이디 중복체크
    def check_same_id(self, join_id):
        self.client_app.send_check_same_id(join_id)

    # 회원가입 승인
    def join_access(self):
        join_id = self.widget_join_page.id.text()
        join_pw = self.widget_join_page.pw.text()
        join_name = self.widget_join_page.name.text()
        join_phone_number = self.widget_join_page.phone_number.text()
        join_email_id = self.widget_join_page.email_id.text()
        join_mail_ad = self.widget_join_page.mail_ad.currentText()
        join_email = f"{join_email_id}@{join_mail_ad}"
        self.client_app.send_join_access(join_id, join_pw, join_name, join_phone_number, join_email)

    # 회원가입 결과
    def join_access_res(self, return_result):
        if return_result:
            QtWidgets.QMessageBox.about(self, "성공", "회원가입 완료")
            self.stackedWidget.setCurrentWidget(self.page)
        else:
            QtWidgets.QMessageBox.about(self, "실패", "회원가입 실패")

    # 로그아웃 버튼 눌렀을시 로그인 화면으로
    def logout_page(self):
        self.stackedWidget.setCurrentWidget(self.page)

    # 메인페이지 설정
    def set_main_page_widget(self):
        before_widget = self.page_3.findChild(BigBookInfo)
        if before_widget is not None:
            before_widget.setParent(None)
            del before_widget
        self.page_3.layout().addWidget(self.widget_header)
        self.page_3.layout().addWidget(self.widget_main_page)
        self.stackedWidget.setCurrentWidget(self.page_3)

    # 검색 페이지 설정
    def set_search_page_widget(self):
        before_widget = self.page_4.findChild(BigBookInfo)
        if before_widget is not None:
            before_widget.setParent(None)
            del before_widget
        self.page_4.layout().addWidget(self.widget_header)
        self.page_4.layout().addWidget(self.widget_search_page)
        self.stackedWidget.setCurrentWidget(self.page_4)

    # 제목으로 책 찾기
    def book_name_search(self, search_contents):
        self.client_app.send_book_name_search(search_contents)

    # 저자로 책 찾기
    def book_writer_search(self, search_contents):
        self.client_app.send_book_writer_search(search_contents)

    # 출판사로 책 찾기
    def book_publisher_search(self, search_contents):
        self.client_app.send_book_publisher_search(search_contents)

    # 찾은 책 목록화
    def search_book(self, return_result):
        self.book_info_list = self.decoder.binary_to_obj(return_result)
        self.widget_search_page.refresh_book_list_widget()
        # print(book_list)
        # self.search_page_book_list = book_list

    # 검색창 목록 초기화
    @staticmethod
    def clear_widget(widget):
        if widget.layout() is not None:
            while widget.layout().count() > 0:
                item = widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

    # 책정보 크게 보기, 교수님에게 물어봤던 문제
    def show_big_book_info(self, book_obj):
        before_widget = self.page_5.findChild(BigBookInfo)
        if before_widget is not None:
            before_widget.setParent(None)
            del before_widget
        widget_big_book_info = BigBookInfo(self, book_obj)
        self.page_5.layout().addWidget(widget_big_book_info)
        self.stackedWidget.setCurrentWidget(self.page_5)

    # 책 대여
    def client_book_rental(self, book_registration_number, rental_day, rental_return_day):
        self.client_app.send_book_rental(book_registration_number, rental_day, rental_return_day)

    # 책 대여 답변 및 최신화
    def client_book_rental_res(self, return_result):
        if return_result == "0":
            QtWidgets.QMessageBox.about(self, "대여 실패", "이미 대여가 완료된 책입니다.")
        else:
            book_obj = self.decoder.binary_to_obj(return_result)
            self.show_big_book_info(book_obj)
            for i in self.widget_search_page.widget_to_add.findChildren(BookInfo):
                if i.book_registration_number.text() == book_obj.book_registration_number:
                    i.book_state.setText("예약가능")
            QtWidgets.QMessageBox.about(self, "대여 성공", "책 대여가 성공적으로 완료되었습니다.")

    # 책 예약
    def client_book_reservation(self, book_registration_number):
        self.client_app.send_book_reservation(book_registration_number)
    
    # 책 예약 결과
    def client_book_reservation_res(self, return_result):
        if return_result == "0":
            QtWidgets.QMessageBox.about(self, "예약 실패", "이미 예약이 완료된 책입니다.")
        else:
            book_obj = self.decoder.binary_to_obj(return_result)
            self.show_big_book_info(book_obj)
            for i in self.widget_search_page.widget_to_add.findChildren(BookInfo):
                if i.book_registration_number.text() == book_obj.book_registration_number:
                    i.book_state.setText("대출,예약 불가능")
            QtWidgets.QMessageBox.about(self, "예약 성공", "책 예약이 성공적으로 완료되었습니다.")
    
    # 문의하기 채팅방 띄우기
    def inquiry_room_open(self):
        self.widget_inquiry_room.show()
