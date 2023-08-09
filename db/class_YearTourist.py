## 년도별 관광객 정보 클래스 ##

class YearTourist:
    """년도별 관광객 정보"""
    def __init__(self, yea_id ,yea_tourist, yea_year, yea_personnel):
        self.yea_id = yea_id                    # 년도 ID
        self.yea_tourist = yea_tourist          # 관광지명
        self.yea_year = yea_year                # 년도
        self.yea_personnel = yea_personnel      # 관광객수

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, YearTourist) and \
                self.yea_id == other.yea_id and \
                self.yea_tourist == other.yea_tourist and \
                self.yea_year == other.yea_year and \
                self.yea_personnel == other.yea_personnel:
            return True
        return False