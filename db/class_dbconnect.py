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
        info_list = self.read_db(1, "TB_REALTY", "REA_TOURIST", f"{nm_}")

        find_result_list = list()
        for info in info_list:
            realty_obj = Realty(*info)
            find_result_list.append(realty_obj)

        self.end_conn()
        return find_result_list

    def find_tourist_info(self, nm_):
        """관광지 정보 반환"""
        info_list = self.read_db(2, "TB_TOURIST_INFO", "TOU_NAME", f"{nm_}")
        print(f"관광지_정보: {info_list}")

        find_result_list = list()
        tourist_obj = TouristInfo(*info_list)
        find_result_list.append(tourist_obj)

        self.end_conn()
        return find_result_list

    def find_store_average(self, nm_):
        """관광지 주변 편의점 평균 정보 반환"""
        # todo: 관광지명 기준으로 편의점 평균 매출 리턴
        info_list = self.read_db(2, "TB_BUSINESS_AVERAGE", "BUS_TOURIST", f"{nm_}")
        print(f"평균_정보: {info_list}")

        find_result_list = list()
        tourist_obj = BusinessAverage(*info_list)
        find_result_list.append(tourist_obj)

        self.end_conn()
        return find_result_list

    def find_infra_info(self, addr_):
        """매물 주변 상권 정보 반환"""
        # todo: 매물 주소를 기준으로 주변 인프라 정보 리턴
        info_list = self.read_db(2, "TB_INFRASTRUCTURE", "INF_ADDRESS", f"{addr_}")
        print(f"주변_상권: {info_list}")

        find_result_list = list()
        tourist_obj = Infrastructure(*info_list)
        find_result_list.append(tourist_obj)

        self.end_conn()
        return find_result_list

    def find_year_peple(self, nm_):
        """년도별 방문 통계 반환"""
        info_list = self.read_db(1, "TB_YEAR_TOURIST", "YEA_TOURIST", f"{nm_}")
        print(f"년도별_방문_통계: {info_list}")

        find_result_list = list()
        for info in info_list:
            realty_obj = YearTourist(*info)
            find_result_list.append(realty_obj)

        self.end_conn()
        return find_result_list

    def read_db(self, num_, table_, column_, condition_):
        """테이블 조회"""
        c = self.start_conn()
        # c.execute(f"select * from \"{table_}\" where \"{column_}\" = '{condition_}'")
        c.execute(f"select * from \"{table_}\" where \"{column_}\" = (%s)", (condition_, ))
        # print(f"조건 : {condition_}")

        if num_ == 1:
            info_list = c.fetchall()
        elif num_ == 2:
            info_list = c.fetchone()

        if len(info_list) == 0:
            return None

        return info_list

    def search_addr(self, realty_obj: Realty):
        """주소 조회 후 관광지명 반환"""
        addr_ = realty_obj.rea_address
        # print(f"{addr_=}")
        tourist_name = self.read_db(1, "TB_REALTY", "REA_ADDRESS", f"{addr_}")
        print(tourist_name[0][1])

        self.find_year_peple(tourist_name[0][1])
        self.find_store_average(tourist_name[0][1])


if __name__ == '__main__':
    db = DBConnector()
    db.test_option = True

    ### test ###
    info_ = db.find_realty_info('에버랜드')
    db.search_addr(info_[0])
