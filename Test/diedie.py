from sklearn.linear_model import LinearRegression
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


class Databases():
    def __init__(self):
        self.conn = psycopg2.connect(host='10.10.20.98', dbname='db_cu', user='postgres', password='1234', port=5432)
        self.cursor = self.conn.cursor()
        self.engine = create_engine(f'postgresql://postgres:1234@10.10.20.98:5432/db_cu')

    def __del__(self):
        self.engine.dispose()


# 데이터 불러오기
db = Databases()
table_name1 = '"TB_TOURIST_INFO"'
table_name2 = '"TB_INFRASTRUCTURE"'
table_name3 = '"TB_INFRASTRUCTURE"'
read_file1 = pd.read_sql(f'select * from {table_name1}', db.engine)
read_file2 = pd.read_sql(f'select * from {table_name2}', db.engine)
place_df = pd.DataFrame(read_file1)
regoin = place_df.TOU_REGION.to_list()
name = place_df.TOU_NAME.to_list()
address = place_df.TOU_ADDRESS.to_list()
ctg = place_df.TOU_CTG.to_list()

inpra_df = pd.DataFrame(read_file2)
mt = inpra_df.INF_MT1.to_list()
cs = inpra_df.INF_CS2.to_list()
ps = inpra_df.INF_PS3.to_list()
sc = inpra_df.INF_SC4.to_list()
ac = inpra_df.INF_AC5.to_list()
pk = inpra_df.INF_PK6.to_list()
ol = inpra_df.INF_OL7.to_list()
sw = inpra_df.INF_SW8.to_list()
bk = inpra_df.INF_BK9.to_list()
ct = inpra_df.INF_CT1.to_list()
ag = inpra_df.INF_AG2.to_list()
po = inpra_df.INF_PO3.to_list()
at = inpra_df.INF_AT4.to_list()
ad = inpra_df.INF_AD5.to_list()
fd = inpra_df.INF_FD6.to_list()
ce = inpra_df.INF_CE7.to_list()
hp = inpra_df.INF_HP8.to_list()
pm = inpra_df.INF_PM9.to_list()

data = {



}

df = pd.DataFrame(data)

# 독립 변수와 종속 변수 분리
X = df[['위치', '인프라', '임대료', '상권 활성화']]  # 독립 변수
y = df['점수']  # 종속 변수

# 다중 선형 회귀 모델 생성
model = LinearRegression()

# 모델 훈련
model.fit(X, y)

# 회귀 계수 확인
coefficients = model.coef_
print('회귀 계수:', coefficients)
