#LocaleSearcher.py
import urllib.request
import json
from map_locale import Locale

key ='5b8a2ea9acc252a5d02768c244cd50bd'
site='https://dapi.kakao.com/v2/local/search/keyword.json'
auth_key="KakaoAK " + key
auth_header = "Authorization"

def SearchLocale(query):
    query = urllib.parse.quote(query)
    query_str = site+"?"+"query="+query
    request = urllib.request.Request(query_str)
    request.add_header(auth_header,auth_key)
    response = urllib.request.urlopen(request) #웹 서버에 요청
    rescode = response.getcode()
    if rescode == 200:
        res = response.read().decode('utf-8')
        jres = json.loads(res)
        if jres == None:
            return []
        locales =[]
        for jloc in jres['documents']:
            locale = Locale.MakeLocale(jloc)
            if locale!=None:
                locales.append(locale)
        return locales
    else:
        return []
