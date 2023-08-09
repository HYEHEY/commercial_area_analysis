class TouristInfo:
    def __init__(self, tou_id, tou_region, tou_name, tou_ctg, tou_address, tou_x, tou_y, tou_personnel):
        self.tou_id = tou_id
        self.tou_region = tou_region
        self.tou_name = tou_name
        self.tou_ctg = tou_ctg
        self.tou_address = tou_address
        self.tou_x = tou_x
        self.tou_y = tou_y
        self.tou_personnel = tou_personnel

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TouristInfo) and \
                self.tou_id == other.tou_id and \
                self.tou_region == other.tou_region and \
                self.tou_name == other.tou_name and \
                self.tou_ctg == other.tou_ctg and \
                self.tou_address == other.tou_address and \
                self.tou_x == other.tou_x and \
                self.tou_y == other.tou_y and \
                self.tou_personnel == other.tou_personnel:
            return True
        return False
