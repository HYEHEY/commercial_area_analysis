## 관광지별 편의점 업소 평균 정보 클래스 ##

class BusinessAverage:
    """관광지별 편의점 업소 평균 정보"""
    def __init__(self, bus_id, bus_tourist, bus_address,
                 bus_business_num, bus_sales, bus_sales_num):
        self.bus_id = bus_id                            # 평균 정보 ID
        self.bus_tourist = bus_tourist                  # 관광지명
        self.bus_address = bus_address                  # 관광지 주소
        self.bus_business_num = bus_business_num        # 편의점 업소수
        self.bus_sales = bus_sales                      # 월평균 매출액
        self.bus_sales_num = bus_sales_num              # 월평균 매출건수

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BusinessAverage) and \
                self.bus_id == other.bus_id and \
                self.bus_tourist == other.bus_tourist and \
                self.bus_address == other.bus_address and \
                self.bus_business_num == other.bus_business_num and \
                self.bus_sales == other.bus_sales and \
                self.bus_sales_num == other.bus_sales_num:
            return True
        return False