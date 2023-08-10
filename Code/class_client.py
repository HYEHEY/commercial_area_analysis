import datetime
import socket
import time
from threading import *

from Code.class_json import *

from db.class_Infrastructure import *
from db.class_TouristInfo import *
from db.class_BusinessAverage import *
from db.class_Realty import *
from db.class_YearTourist import *
from db.class_RegionTourist import *


class ClientApp:
    HOST = '10.10.20.115'
    # HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    tourist_name = "tourist_name"
    realty_info = "realty_info"

    def __init__(self):
        self.user_id = None
        self.client_socket = None
        self.config = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()

        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def set_widget(self, widget_):
        self.client_widget = widget_

    def send_tourist_name_access(self, tourist_name):
        """관광지 명 서버로 보내기"""
        data_msg = tourist_name
        header_data = self.tourist_name
        self.fixed_volume(header_data, data_msg)

    def fixed_volume(self, header, data):
        """데이터 길이 맞춰서 서버로 전송"""
        header_msg = f"{header:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg = f"{data:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)

    def receive_message(self):
        """서버에서 정보 받아옴"""
        while True:
            return_result_ = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            response_header = return_result_[:self.HEADER_LENGTH].strip()
            response_data = return_result_[self.HEADER_LENGTH:].strip()
            # 관광지 명
            if response_header == self.tourist_name:
                self.client_widget.tourist_name_signal.emit(response_data)

            # 부동산 정보
            if response_header == self.realty_info:
                self.client_widget.realty_info_signal.emit(response_data)

