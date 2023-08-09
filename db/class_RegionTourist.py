## 지역 정보 클래스 ##

class RegionTourist:
    """지역 정보"""
    def __init__(self, reg_id, reg_name):
        self.reg_id = reg_id            # 지역 ID
        self.reg_name = reg_name        # 지역명

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RegionTourist) and \
                self.reg_id == other.reg_id and \
                self.reg_name == other.reg_name:
            return True
        return False