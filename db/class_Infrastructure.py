class Infrastructure:
    def __init__(self, INF_ID, INF_TOURIST, INF_ADDRESS, INF_MT1,
                 INF_CS2, INF_PS3, INF_SC4, INF_AC5, INF_PK6, INF_OL7,
                 INF_SW8, INF_BK9, INF_CT1, INF_AG2, INF_PO3, INF_AT4,
                 INF_AD5, INF_FD6, INF_CE7, INF_HP8, INF_PM9):
        self.INF_ID = INF_ID
        self.INF_TOURIST = INF_TOURIST
        self.INF_ADDRESS = INF_ADDRESS
        self.INF_MT1 = INF_MT1
        self.INF_CS2 = INF_CS2
        self.INF_PS3 = INF_PS3
        self.INF_SC4 = INF_SC4
        self.INF_AC5 = INF_AC5
        self.INF_PK6 = INF_PK6
        self.INF_OL7 = INF_OL7
        self.INF_SW8 = INF_SW8
        self.INF_BK9 = INF_BK9
        self.INF_CT1 = INF_CT1
        self.INF_AG2 = INF_AG2
        self.INF_PO3 = INF_PO3
        self.INF_AT4 = INF_AT4
        self.INF_AD5 = INF_AD5
        self.INF_FD6 = INF_FD6
        self.INF_CE7 = INF_CE7
        self.INF_HP8 = INF_HP8
        self.INF_PM9 = INF_PM9

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, Infrastructure) and \
                self.INF_ID == other.INF_ID and \
                self.INF_TOURIST == other.INF_TOURIST and \
                self.INF_ADDRESS == other.INF_ADDRESS and \
                self.INF_MT1 == other.INF_MT1 and \
                self.INF_CS2 == other.INF_CS2 and \
                self.INF_PS3 == other.INF_PS3 and \
                self.INF_SC4 == other.INF_SC4 and \
                self.INF_AC5 == other.INF_AC5 and \
                self.INF_PK6 == other.INF_PK6 and \
                self.INF_OL7 == other.INF_OL7 and \
                self.INF_CS2 == other.INF_CS2 and \
                self.INF_CS2 == other.INF_CS2 and \
                self.INF_CS2 == other.INF_CS2 and \
                self.INF_CS2 == other.INF_CS2 and \
                self.INF_PS3 == other.INF_PS3:
            return True
        return False