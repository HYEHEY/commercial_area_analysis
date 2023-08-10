## DB 컨트롤러 클래스 ##

import psycopg2 as pg
from sqlalchemy import create_engine

from class_RegionTourist import RegionTourist
from class_TouristInfo import TouristInfo
from class_Realty import Realty
from class_BusinessAverage import BusinessAverage
from class_Infrastructure import Infrastructure
from class_YearTourist import YearTourist


class DBConnector:
    """DB"""
    _instance = None

    def __new__(cls, test_option=None):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=None):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        """DB 접속"""
        if self.test_option is True:
            self.conn = pg.connect(host="10.10.20.98",
                                   dbname="db_cu",
                                   user="postgres",
                                   password="1234",
                                   port=5432)
            # print("test_option is True")
        else:
            # self.conn = pg.connect("main_db.db")
            print("test_option is False")
        self.engine = create_engine(f'postgresql://postgres:1234@10.10.20.98:5432/db_cu')

        return self.conn.cursor()

    def end_conn(self):
        """DB 종료 및 초기화"""
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        """DB 커밋"""
        if self.conn is not None:
            self.conn.commit()
        else:
            raise f'connot commit datatbase! {self.__name__}'

    ## read ==================================================================================

    def find_realty_info(self, nm_):
        """부동산 정보 반환"""
        c = self.start_conn()
        c.execute(f"select * from \"TB_REALTY\" where \"REA_TOURIST\" = '{nm_}'")
        info_list = c.fetchall()
        # 부동산 ID, 관광지명, 부동산 주소, 상가 종류, 경도, 위도, 계약 면적, 전역 면적, 부동산 분류, 임대료, 보증금, 매매가

        if len(info_list) == 0:
            return None

        find_result_list = list()
        for info in info_list:
            # print(f"{info=}")
            realty_obj = Realty(*info)
            find_result_list.append(realty_obj)

        self.end_conn()
        return find_result_list

    def find_tourist_info(self, nm_):
        """관광지 정보 반환"""
        c = self.start_conn()
        c.execute(f"select * from \"TB_TOURIST_INFO\" where \"TOU_NAME\" = '{nm_}')")
        # 관광지 ID, 지역명, 관광지명, 주소, 분류, 경도, 위도, 관광객수

        info_list = c.fetchone()
        print(f"관광지명 : {nm_}")

        if len(info_list) == 0:
            return None

        find_result_list = list()
        tourist_obj = TouristInfo(*info_list)
        find_result_list.append(tourist_obj)

        self.end_conn()
        return find_result_list

    def find_year_peple(self, addr_):
        """년도별 방문 통계 반환"""
        # todo: 관광지명 기준으로 년도별 방문 통계 리턴
        pass

    def find_store_average(self):
        """관광지 주변 편의점 평균 정보 반환"""
        # todo: 관광지명 기준으로 편의점 평균 매출 리턴
        pass

    def find_infra_info(self):
        """매물 주변 상권 정보 반환"""
        # todo: 매물 주소를 기준으로 주변 인프라 정보 리턴
        pass


if __name__ == '__main__':
    db = DBConnector()
    db.test_option = True

    ### test ###
    a = db.find_realty_info('안목해변')
    # a = db.find_tourist_info('수성못')
    print(a)
