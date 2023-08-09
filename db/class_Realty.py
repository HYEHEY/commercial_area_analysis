## 부동산 정보 클래스 ##

class Realty:
    """부동산 정보"""
    def __init__(self, rea_id, rea_rourist, rea_address, rea_store_ctg,
                 rea_x, rea_y, rea_contract_area, rea_dedicaed_area,
                 rea_realty_ctg, reg_rantal_price, reg_deposit, reg_selling_price):
        self.rea_id = rea_id                            # 부동산 ID
        self.rea_rourist = rea_rourist                  # 관광지명
        self.rea_address = rea_address                  # 부동산 주소
        self.rea_store_ctg = rea_store_ctg              # 상가 종류(일반상가, 복합상가, 단지내상가)
        self.rea_x = rea_x                              # 경도
        self.rea_y = rea_y                              # 위도
        self.rea_contract_area = rea_contract_area      # 계약 면적
        self.rea_dedicaed_area = rea_dedicaed_area      # 전용 면적
        self.rea_realty_ctg = rea_realty_ctg            # 부동산 분류(임대, 매매)
        self.reg_rantal_price = reg_rantal_price        # 임대료
        self.reg_deposit = reg_deposit                  # 보증금
        self.reg_selling_price = reg_selling_price      # 매매가

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, Realty) and \
                self.rea_id == other.rea_id and \
                self.rea_rourist == other.rea_rourist and \
                self.rea_address == other.rea_address and \
                self.rea_store_ctg == other.rea_store_ctg and \
                self.rea_x == other.rea_x and \
                self.rea_y == other.rea_y and \
                self.rea_contract_area == other.rea_contract_area and \
                self.rea_dedicaed_area == other.rea_dedicaed_area and \
                self.rea_realty_ctg == other.rea_realty_ctg and \
                self.reg_rantal_price == other.reg_rantal_price and \
                self.reg_deposit == other.reg_deposit and \
                self.reg_selling_price == other.reg_selling_price:
            return True
        return False
