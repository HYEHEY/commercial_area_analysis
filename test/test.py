import psycopg2 as pg

conn = pg.connect(host="10.10.20.98", dbname="db_cu", user="postgres", password="1234", port="5432")
c = conn.cursor()

c.execute(f"select * from \"TB_BUSINESS_AVERAGE\"")
print(c.fetchall())

conn.close()