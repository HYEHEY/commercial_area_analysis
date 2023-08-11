## 주변 상권 정보 클래스 ##

class Infrastructure:
    """주변 상권 정보"""
    def __init__(self, inf_id, inf_tourist, inf_address,
                 inf_cp1, inf_lf2, inf_sp3, inf_sc4, inf_ac5, inf_pk6,
                 inf_ol7, inf_sw8, inf_bk9, inf_ct1, inf_ag2, inf_po3,
                 inf_at4, inf_ad5, inf_fd6, inf_ce7, inf_hp8, inf_pm9,
                 inf_fs1, inf_bt2, inf_bd3, inf_rl4, inf_rf5):
        self.inf_id = inf_id                # 부동산 ID
        self.inf_tourist = inf_tourist      # 관광지명
        self.inf_address = inf_address      # 부동산 주소
        self.inf_cp1 = inf_cp1              # 경쟁업체
        self.inf_lf2 = inf_lf2              # 여가시설
        self.inf_sp3 = inf_sp3              # 스포츠
        self.inf_sc4 = inf_sc4              # 학교
        self.inf_ac5 = inf_ac5              # 학원
        self.inf_pk6 = inf_pk6              # 주차장
        self.inf_ol7 = inf_ol7              # 주유소, 충전소
        self.inf_sw8 = inf_sw8              # 지하철역
        self.inf_bk9 = inf_bk9              # 은행
        self.inf_ct1 = inf_ct1              # 문화시설
        self.inf_ag2 = inf_ag2              # 중개업소
        self.inf_po3 = inf_po3              # 공공기관
        self.inf_at4 = inf_at4              # 관광명소
        self.inf_ad5 = inf_ad5              # 숙박
        self.inf_fd6 = inf_fd6              # 음식점
        self.inf_ce7 = inf_ce7              # 카페
        self.inf_hp8 = inf_hp8              # 병원
        self.inf_pm9 = inf_pm9              # 약국
        self.inf_fs1 = inf_fs1              # 패션
        self.inf_bt2 = inf_bt2              # 미용
        self.inf_bd3 = inf_bd3              # 빌딩
        self.inf_rl4 = inf_rl4              # 종교
        self.inf_rf5 = inf_rf5              # 주거시설

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, Infrastructure) and \
                self.inf_id == other.inf_id and \
                self.inf_tourist == other.inf_tourist and \
                self.inf_address == other.inf_address and \
                self.inf_cp1 == other.inf_mt1 and \
                self.inf_lf2 == other.inf_cs2 and \
                self.inf_sp3 == other.inf_ps3 and \
                self.inf_sc4 == other.inf_sc4 and \
                self.inf_ac5 == other.inf_ac5 and \
                self.inf_pk6 == other.inf_pk6 and \
                self.inf_ol7 == other.inf_ol7 and \
                self.inf_sw8 == other.inf_sw8 and \
                self.inf_bk9 == other.inf_bk9 and \
                self.inf_ct1 == other.inf_ct1 and \
                self.inf_ag2 == other.inf_ag2 and \
                self.inf_po3 == other.inf_po3 and \
                self.inf_at4 == other.inf_at4 and \
                self.inf_ad5 == other.inf_ad5 and \
                self.inf_fd6 == other.inf_fd6 and \
                self.inf_ce7 == other.inf_ce7 and \
                self.inf_hp8 == other.inf_hp8 and \
                self.inf_pm9 == other.inf_pm9 and \
                self.inf_fs1 == other.inf_fs1 and \
                self.inf_bt2 == other.inf_bt2 and \
                self.inf_bd3 == other.inf_bd3 and \
                self.inf_rl4 == other.inf_rl4 and \
                self.inf_rf5 == other.inf_rf5:
            return True
        return False
