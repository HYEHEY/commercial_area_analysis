import os
import sqlite3
import pandas as pd
import requests
from urllib.parse import urlparse

con = sqlite3.connect('./data.db')

df_1 = pd.read_sql("select * from TB_", con)

df_var = df_1.values
df_var = df_var.tolist()

for i in df_var:
    print(f"{i=}")
    # for j in i[1:]:     # idx 0은 id 값으로 넣기(순서정렬을 위해서)

    if i[3] != None:      # 주소 != None
        # print(f"{i[3]=}")
        address = i[3]
        # print(address)
        if address == '-':  # 주소 행에 "-"이 있을 경우 -> 이 부분은 입맛에 맞게 수정 가능
            lng = 'Null'  # 경도
            lat = 'Null'  # 위도

            con.execute(f'update tb_daegu set (경도, 위도) = ({lng}, {lat}) where 주소 = "-"')

            con.commit()
        else:
            url = f"https://dapi.kakao.com/v2/local/search/address.json?query={address}"

            result = requests.get(urlparse(url).geturl(),
                                  headers={"Authorization": "KakaoAK 5b8a2ea9acc252a5d02768c244cd50bd"}).json()
            # result={'documents': [{'address': {'address_name': '울산 남구 삼산동 1571-11', 'b_code': '3114010600', 'h_code': '3114057000', 'main_address_no': '1571', 'mountain_yn': 'N', 'region_1depth_name': '울산', 'region_2depth_name': '남구', 'region_3depth_h_name': '삼산동', 'region_3depth_name': '삼산동', 'sub_address_no': '11', 'x': '129.337745957737', 'y': '35.5407109720703'}, 'address_name': '울산 남구 돋질로306번길 32', 'address_type': 'ROAD_ADDR', 'road_address': {'address_name': '울산 남구 돋질로306번길 32', 'building_name': '', 'main_building_no': '32', 'region_1depth_name': '울산', 'region_2depth_name': '남구', 'region_3depth_name': '삼산동', 'road_name': '돋질로306번길', 'sub_building_no': '', 'underground_yn': 'N', 'x': '129.337745957737', 'y': '35.5407109720703', 'zone_no': '44705'}, 'x': '129.337745957737', 'y': '35.5407109720703'}], 'meta': {'is_end': True, 'pageable_count': 1, 'total_count': 1}}

            print(f'{result=}')
            # print(json.dump(result, indent=4, ensure_ascii=False, fp=None))

            lng = result["documents"][0]["y"]  # 경도
            lat = result["documents"][0]["x"]  # 위도

            con.execute(f'update tb_daegu set (경도, 위도) = ({lng}, {lat}) where 주소 = "{address}"')

            # print(address)
            print(f"위도 : {lat}\n경도 : {lng}")

            con.commit()