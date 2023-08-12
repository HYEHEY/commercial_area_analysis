import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


class Databases:
    def __init__(self):
        self.conn = psycopg2.connect(host='10.10.20.98', dbname='db_cu', user='postgres', password='1234', port=5432)
        self.cursor = self.conn.cursor()
        self.engine = create_engine(f'postgresql://postgres:1234@10.10.20.98:5432/db_cu')

    def __del__(self):
        self.engine.dispose()


scaler = MinMaxScaler()
# 데이터 불러오기
db = Databases()
table_name1 = '"TB_TOURIST_INFO"'
table_name2 = '"TB_INFRASTRUCTURE"'
table_name3 = '"TB_REALTY"'
table_name4 = '"TB_BUSINESS_AVERAGE"'
read_file1 = pd.read_sql('select a."TOU_PERSONNEL" FROM "TB_TOURIST_INFO" a INNER '
                         'JOIN "TB_REALTY" b ON a."TOU_NAME" = b."REA_TOURIST"', db.engine)
read_file2 = pd.read_sql(f'select "INF_CP1", "INF_LF2", "INF_SC3", "INF_PK4", "INF_SU5", "INF_CT6", "INF_AD7", '
                         f'"INF_HC8", "INF_BD9", "INF_RF0" from {table_name2}', db.engine)
read_file3 = pd.read_sql(f'select "REA_DEDICAED_AREA" from {table_name3}', db.engine)
read_file4 = pd.read_sql('select a."REG_SELLING_PRICE", b."BUS_BUSINESS_NUM", b."BUS_SALES", '
                         'b."BUS_SALES_NUM" FROM "TB_REALTY" a INNER JOIN "TB_BUSINESS_AVERAGE" b ON '
                         'a."REA_TOURIST" = b."BUS_TOURIST"', db.engine)

place_df = pd.DataFrame(read_file1)
place_scaled = scaler.fit_transform(place_df)
place_df_scaled = pd.DataFrame(place_scaled, columns=place_df.columns)
people_num = place_df_scaled.TOU_PERSONNEL.to_list()

inpra_df = pd.DataFrame(read_file2)
inpra_scaled = scaler.fit_transform(inpra_df)
inpra_df_scaled = pd.DataFrame(inpra_scaled, columns=inpra_df.columns)
inpra_df_scaled.to_csv('C:/Users/KDT115/Desktop/commercial_area_analysis/살려줘.csv')
print('시설 정규화 점수 \n', inpra_df_scaled)
cp = list()
CP = inpra_df_scaled.INF_CP1.to_list()
for i in CP:
    i = i * -1
    cp.append(i)
LF = inpra_df_scaled.INF_LF2.to_list()
SC = inpra_df_scaled.INF_SC3.to_list()
PK = inpra_df_scaled.INF_PK4.to_list()
SU = inpra_df_scaled.INF_SU5.to_list()
CT = inpra_df_scaled.INF_CT6.to_list()
AD = inpra_df_scaled.INF_AD7.to_list()
HC = inpra_df_scaled.INF_HC8.to_list()
BD = inpra_df_scaled.INF_BD9.to_list()
RF = inpra_df_scaled.INF_RF0.to_list()


bu_df = pd.DataFrame(read_file3)
bu_scaled = scaler.fit_transform(bu_df)
bu_df_scaled = pd.DataFrame(bu_scaled, columns=bu_df.columns)
size_ = bu_df_scaled.REA_DEDICAED_AREA.to_list()

aver = pd.DataFrame(read_file4)
aver_scaled = scaler.fit_transform(aver)
aver_df_scaled = pd.DataFrame(aver_scaled, columns=aver.columns)
sales = aver_df_scaled.BUS_SALES.to_list()
sales_num = aver_df_scaled.BUS_SALES_NUM.to_list()

data = {
    # '지역명': regoin,
    # '관광지명': name_,
    # '관광지 주소': address,
    # '관광지 분류': ctg,
    # '인프라': total_inpra,
    # '월세': r_price,
    # '보증금': price,
    # '경쟁업체': cp,
    '여가시설': LF,
    '교육 및 교통 시설': SC,
    '주차시설': PK,
    '상업시설': SU,
    '관광 및 문화 시설': CT,
    '숙박': AD,
    '건강 및 종교 시설': HC,
    '빌딩': BD,
    '주거시설': RF,
    # '전역 면적': size_,
    '월평균 매출액': sales,
    # '월평균 매출건수': sales_num,
    # '관광객수': people_num,
}

df = pd.DataFrame(data)

# 독립 변수와 종속 변수 분리
X = df[['여가시설', '교육 및 교통 시설', '주차시설', '상업시설', '관광 및 문화 시설', '숙박', '건강 및 종교 시설', '빌딩', '주거시설']]  # 독립 변수
y = df['월평균 매출액']  # 종속 변수

# 다중 선형 회귀 모델 생성
model = LinearRegression()

# 모델 훈련
model.fit(X, y)

# 회귀 계수 확인
coefficients = model.coef_
print('회귀 계수:', coefficients)
result1 = sum(coefficients)
print(result1)
# 회귀 계수를 양수로 조정
positive_coefs = np.abs(model.coef_)

# 양수로 조정된 회귀 계수 출력
print("Positive Coefficients:", positive_coefs)
result1 = sum(positive_coefs)
print(result1)