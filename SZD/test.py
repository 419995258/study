sql = "create table NB_XX_2018(id VARCHAR2(255),"
sql = sql + ""
col = "X_"
for r in range(1, 374):
    sql = sql + col + str(r) + " VARCHAR2(255),"

sql = sql + " primary key (id) )"
print sql