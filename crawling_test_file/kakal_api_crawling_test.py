import json
import requests
import pandas as pd


class KakaoLocalAPI:
    """
    Kakao Local API 컨트롤러
    """

    def __init__(self, rest_api_key):
        """
        Rest API키 초기화 및 기능 별 URL 설정
        """

        # REST API 키 설정
        self.rest_api_key = rest_api_key
        self.headers = {"Authorization": "KakaoAK {}".format(rest_api_key)}

        # 서비스 별 URL 설정

        # 01 주소 검색
        self.URL_01 = "https://dapi.kakao.com/v2/local/search/address.json"
        # 02 좌표-행정구역정보 변환
        self.URL_02 = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json"
        # 03 좌표-주소 변환
        self.URL_03 = "https://dapi.kakao.com/v2/local/geo/coord2address.json"
        # 04 좌표계 변환
        self.URL_04 = "https://dapi.kakao.com/v2/local/geo/transcoord.json"
        # 05 키워드 검색
        self.URL_05 = "https://dapi.kakao.com/v2/local/search/keyword.json"
        # 06 카테고리 검색
        self.URL_06 = "https://dapi.kakao.com/v2/local/search/category.json"

    def search_address(self, query, analyze_type=None, page=None, size=None):
        """
        01 주소 검색
        """
        params = {"query": f"{query}"}

        if analyze_type != None:
            params["analyze_type"] = f"{analyze_type}"

        if page != None:
            params['page'] = f"{page}"

        if size != None:
            params['size'] = f"{size}"

        res = requests.get(self.URL_01, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_coord2regioncode(self, x, y, input_coord=None, output_coord=None):
        """
        02 좌표-행정구역정보 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        if output_coord != None:
            params['output_coord'] = f"{output_coord}"

        res = requests.get(self.URL_02, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_coord2address(self, x, y, input_coord=None):
        """
        03 좌표-주소 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        res = requests.get(self.URL_03, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_transcoord(self, x, y, output_coord, input_coord=None):
        """
        04 좌표계 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}",
                  "output_coord": f"{output_coord}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        res = requests.get(self.URL_04, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def search_keyword(self, query, category_group_code=None, x=None, y=None, radius=None, rect=None, page=None,
                       size=None, sort=None):
        """
        05 키워드 검색
        """
        params = {"query": f"{query}"}

        if category_group_code != None:
            params['category_group_code'] = f"{category_group_code}"
        if x != None:
            params['x'] = f"{x}"
        if y != None:
            params['y'] = f"{y}"
        if radius != None:
            params['radius'] = f"{radius}"
        if rect != None:
            params['rect'] = f"{rect}"
        if page != None:
            params['page'] = f"{page}"
        if size != None:
            params['size'] = f"{params}"
        if sort != None:
            params['sort'] = f"{sort}"

        res = requests.get(self.URL_05, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def search_category(self, category_group_code, x, y, radius=None, rect=None, page=None, size=None, sort=None):
        """
        06 카테고리 검색
        """
        params = {'category_group_code': f"{category_group_code}",
                  'x': f"{x}",
                  'y': f"{y}"}

        if radius != None:
            params['radius'] = f"{radius}"
        if rect != None:
            params['rect'] = f"{rect}"
        if page != None:
            params['page'] = f"{page}"
        if size != None:
            params['size'] = f"{size}"
        if sort != None:
            params['sort'] = f"{sort}"

        res = requests.get(self.URL_06, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document


# REST API 키
rest_api_key = "52756ac9cbee83797b5dd4e41ff78344"  # 여기서 개인적으로 받은 카카오 api 키 발급받아야 함

kakao = KakaoLocalAPI(rest_api_key)

df = pd.read_csv('price_output.csv', encoding='utf-8')

INF_ID = list()
INF_TOURIST = list()
INF_ADDRESS = list()
INF_CP1_list = list()
INF_LF2_list = list()
INF_SC3_list = list()
INF_PK4_list = list()
INF_SU5_list = list()
INF_CT6_list = list()
INF_AD7_list = list()
INF_HC8_list = list()
INF_BD9_list = list()
INF_RF0_list = list()

for i in range(len(df)):
    id_ = df.loc[i, 'INF_ID']
    tourist = df.loc[i, 'INF_TOURIST']
    addr = df.loc[i, 'INF_ADDRESS']
    x_coordinate = df.loc[i, 'INF_X']
    y_coordinate = df.loc[i, 'INF_Y']
    result_01 = kakao.search_keyword(query=addr, x=x_coordinate, y=y_coordinate, radius=330)
    INF_CP1 = 0
    INF_LF2 = 0
    INF_SC3 = 0
    INF_PK4 = 0
    INF_SU5 = 0
    INF_CT6 = 0
    INF_AD7 = 0
    INF_HC8 = 0
    INF_BD9 = 0
    INF_RF0 = 0
    test = result_01['documents']
    print(test)
    for j in range(len(test)):
        category_group_code = test[j]['category_group_code']
        category_name = test[j]['category_name']
        place_name = test[j]['place_name']
        if (category_group_code == 'MT1') or (category_group_code == 'CS2') or ('다이소' in category_name) or ('올리브영' in category_name) or ('마트' in category_name):
            INF_CP1 += 1
        if ('여가시설' in category_name) or ('문화시설' in category_name) or ('스포츠' in category_name):
            INF_LF2 += 1
        if (category_group_code == 'SC4') or ('학교' in category_name) or (category_group_code == 'AC5') or ('학습시설' in category_name) or (category_group_code == 'SW8') or (category_group_code == 'PO3') or ('학원' in category_name) or ('학교' in place_name) or ('학원' in place_name):
            INF_SC3 += 1
        if category_group_code == 'PK6':
            INF_PK4 += 1
        if (category_group_code == 'OL7') or (category_group_code == 'FD6') or (category_group_code == 'CE7') or ('음식점' in category_name) or ('패션' in category_name) or ('미용' in category_name):
            INF_SU5 += 1
        if category_group_code == 'AT4' or category_group_code == 'CT1':
            INF_CT6 += 1
        if (category_group_code == 'AD5') or ('호텔' in place_name) or ('모텔' in place_name) or ('팬션' or place_name) or ('리조트' in place_name) or ('게스트하우스' in place_name) or ('에어비앤비' in place_name) or ('한옥스테이' in place_name) or ('레지던스' in place_name):
            INF_AD7 += 1
        if (category_group_code == 'HP8') or ('의료' in category_name) or (category_group_code == 'PM9') or ('종교' in category_name):
            INF_HC8 += 1
        if '빌딩' in category_name:
            INF_BD9 += 1
        if ('주거시설' in category_name) or ('아파트' in place_name) or ('빌라' in place_name) or ('원룸' in place_name):
            INF_RF0 += 1

    INF_ID.append(id_)
    INF_TOURIST.append(tourist)
    INF_ADDRESS.append(addr)
    INF_CP1_list.append(INF_CP1)
    INF_LF2_list.append(INF_LF2)
    INF_SC3_list.append(INF_SC3)
    INF_PK4_list.append(INF_PK4)
    INF_SU5_list.append(INF_SU5)
    INF_CT6_list.append(INF_CT6)
    INF_AD7_list.append(INF_AD7)
    INF_HC8_list.append(INF_HC8)
    INF_BD9_list.append(INF_BD9)
    INF_RF0_list.append(INF_RF0)

df_new = pd.DataFrame(
    {
        "INF_ID": INF_ID,
        "INF_TOURIST": INF_TOURIST,
        "INF_ADDRESS": INF_ADDRESS,
        "INF_CP1": INF_CP1_list,
        "INF_LF2": INF_LF2_list,
        "INF_SC3": INF_SC3_list,
        "INF_PK4": INF_PK4_list,
        "INF_SU5": INF_SU5_list,
        "INF_CT6": INF_CT6_list,
        "INF_AD7": INF_AD7_list,
        "INF_HC8": INF_HC8_list,
        "INF_BD9": INF_BD9_list,
        "INF_RF0": INF_RF0_list
    }
)
df_new.to_csv('Jeju_TB_INFRASTRUCTURE.csv', index=False)
