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
read_file2 = pd.read_sql(f'select "INF_CP1", "INF_LF2", "INF_SP3", "INF_SC4", "INF_AC5", "INF_PK6", "INF_OL7", '
                         f'"INF_SW8", "INF_BK9", "INF_CT1", "INF_AG2", "INF_PO3", "INF_AT4", "INF_AD5", "INF_FD6", '
                         f'"INF_CE7", "INF_HP8", "INF_PM9", "INF_FS1", "INF_BT2", "INF_BD3", "INF_RL4", "INF_RF5" from '
                         f'{table_name2}', db.engine)
read_file3 = pd.read_sql(f'select "REA_DEDICAED_AREA" from {table_name3}', db.engine)
read_file4 = pd.read_sql('select a."REG_SELLING_PRICE", b."BUS_BUSINESS_NUM", b."BUS_SALES", '
                         'b."BUS_SALES_NUM" FROM "TB_REALTY" a INNER JOIN "TB_BUSINESS_AVERAGE" b ON '
                         'a."REA_TOURIST" = b."BUS_TOURIST"', db.engine)

place_df = pd.DataFrame(read_file1)
place_scaled = scaler.fit_transform(place_df)
place_df_scaled = pd.DataFrame(place_scaled, columns=place_df.columns)
people_num = place_df_scaled.TOU_PERSONNEL.to_list()
print(people_num)

inpra_df = pd.DataFrame(read_file2)
inpra_scaled = scaler.fit_transform(inpra_df)
inpra_df_scaled = pd.DataFrame(inpra_scaled, columns=inpra_df.columns)
cp = list()
cp_1 = inpra_df_scaled.INF_CP1.to_list()
for i in cp_1:
    i = i * -1
    cp.append(i)
lf = inpra_df_scaled.INF_LF2.to_list()
sp = inpra_df_scaled.INF_SP3.to_list()
sc = inpra_df_scaled.INF_SC4.to_list()
ac = inpra_df_scaled.INF_AC5.to_list()
pk = inpra_df_scaled.INF_PK6.to_list()
ol = inpra_df_scaled.INF_OL7.to_list()
sw = inpra_df_scaled.INF_SW8.to_list()
bk = inpra_df_scaled.INF_BK9.to_list()
ct = inpra_df_scaled.INF_CT1.to_list()
ag = inpra_df_scaled.INF_AG2.to_list()
po = inpra_df_scaled.INF_PO3.to_list()
at = inpra_df_scaled.INF_AT4.to_list()
ad = inpra_df_scaled.INF_AD5.to_list()
fd = inpra_df_scaled.INF_FD6.to_list()
ce = inpra_df_scaled.INF_CE7.to_list()
hp = inpra_df_scaled.INF_HP8.to_list()
pm = inpra_df_scaled.INF_PM9.to_list()
fs = inpra_df_scaled.INF_FS1.to_list()
bt = inpra_df_scaled.INF_BT2.to_list()
bd = inpra_df_scaled.INF_BD3.to_list()
rl = inpra_df_scaled.INF_RL4.to_list()
rf = inpra_df_scaled.INF_RF5.to_list()
total_inpra = list()
for cp, lf, sp, sc, ac, pk, ol, sw, bk, ct, ag, po, at, ad, fd, ce, hp, pm, fs, bt, bd, rl, rf in zip(cp, lf, sp, sc, ac, pk,
                                                                                                  ol, sw, bk, ct, ag,
                                                                                                  po, at, ad, fd, ce,
                                                                                                  hp, pm, fs, bt, bd,
                                                                                                  rl, rf):
    total = cp+lf+sp + sc + ac + pk + ol + sw + bk + ct + ag + po + at + ad + hp + pm + fs + bt + bd + rl + rf
    total_inpra.append(total)
print(total_inpra)

bu_df = pd.DataFrame(read_file3)
bu_scaled = scaler.fit_transform(bu_df)
bu_df_scaled = pd.DataFrame(bu_scaled, columns=bu_df.columns)
size_ = bu_df_scaled.REA_DEDICAED_AREA.to_list()
print(size_[0])

aver = pd.DataFrame(read_file4)
aver_scaled = scaler.fit_transform(aver)
aver_df_scaled = pd.DataFrame(aver_scaled, columns=aver.columns)
sales = aver_df_scaled.BUS_SALES.to_list()
sales_num = aver_df_scaled.BUS_SALES_NUM.to_list()
print(sales_num[0])

data = {
    # '지역명': regoin,
    # '관광지명': name_,
    # '관광지 주소': address,
    # '관광지 분류': ctg,
    '인프라': total_inpra,
    # '월세': r_price,
    # '보증금': price,
    '전역 면적': size_,
    '월평균 매출액': sales,
    '월평균 매출건수': sales_num,
    '관광객수': people_num,
}

df = pd.DataFrame(data)

# 독립 변수와 종속 변수 분리
X = df[["인프라", '전역 면적', '월평균 매출액', '월평균 매출건수']]  # 독립 변수
y = df['관광객수']  # 종속 변수

# 다중 선형 회귀 모델 생성
model = LinearRegression()

# 모델 훈련
model.fit(X, y)

# 회귀 계수 확인
coefficients = model.coef_
print('회귀 계수:', coefficients)
