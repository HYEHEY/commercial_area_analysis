#Locale.py
import json


class Locale:
    @staticmethod
    def MakeLocale(post):
        try:
            pn = post['place_name']
            x = post['x']
            y = post['y']
            return Locale(pn, x, y)
        except:
            return None

    def __init__(self, pn, x, y):
        self.pn = pn
        self.x = x
        self.y = y
