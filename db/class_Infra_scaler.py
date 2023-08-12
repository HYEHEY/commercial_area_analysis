## 주변 상권 정보 클래스 ##

class InfraScaler:
    """주변 상권 정보"""
    def __init__(self, inf_id, inf_cp1, inf_lf2, inf_sc3, inf_pk4, inf_su5, inf_ct6, inf_ad7, inf_hc8, inf_bd9, inf_rf0):
        self.inf_id = inf_id                # 부동산 ID
        self.inf_cp1 = inf_cp1              # 경쟁업체
        self.inf_lf2 = inf_lf2              # 여가시설
        self.inf_sc3 = inf_sc3              # 교육 및 교통 시설
        self.inf_pk4 = inf_pk4              # 주차시설
        self.inf_su5 = inf_su5              # 상업시설
        self.inf_ct6 = inf_ct6              # 관광 및 문화 시설
        self.inf_ad7 = inf_ad7              # 숙박
        self.inf_hc8 = inf_hc8              # 건강 및 종교 시설
        self.inf_bd9 = inf_bd9              # 빌딩
        self.inf_rf0 = inf_rf0              # 주거시설


    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, InfraScaler) and \
                self.inf_cp1 == other.inf_cp1 and \
                self.inf_lf2 == other.inf_lf2 and \
                self.inf_sc3 == other.inf_sc3 and \
                self.inf_pk4 == other.inf_pk4 and \
                self.inf_su5 == other.inf_su5 and \
                self.inf_ct6 == other.inf_ct6 and \
                self.inf_ad7 == other.inf_ad7 and \
                self.inf_hc8 == other.inf_hc8 and \
                self.inf_bd9 == other.inf_bd9 and \
                self.inf_rf0 == other.inf_rf0:
            return True
        return False
