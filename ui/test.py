import map_localesearcher
from map_localesearcher import *
query = input("지역 검색어:")
locales = SearchLocale(query)
for locale in locales:
    print("{0}({1},{2})".format(locale.pn,locale.x,locale.y))
