## 관광지 정보 클래스 ##

class TouristInfo:
    """관광지 정보"""
    def __init__(self, tou_id, tou_region, tou_name, tou_address, tou_ctg, tou_x, tou_y, tou_personnel):
        self.tou_id = tou_id                    # 관광지 ID
        self.tou_region = tou_region            # 지역명
        self.tou_name = tou_name                # 관광지명
        self.tou_address = tou_address          # 관광지 주소
        self.tou_ctg = tou_ctg                  # 관광지 분류(백화점, 자연경관, ...)
        self.tou_x = tou_x                      # 경도
        self.tou_y = tou_y                      # 위도
        self.tou_personnel = tou_personnel      # 관광객수

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TouristInfo) and \
                self.tou_id == other.tou_id and \
                self.tou_region == other.tou_region and \
                self.tou_name == other.tou_name and \
                self.tou_address == other.tou_address and \
                self.tou_ctg == other.tou_ctg and \
                self.tou_x == other.tou_x and \
                self.tou_y == other.tou_y and \
                self.tou_personnel == other.tou_personnel:
            return True
        return False
