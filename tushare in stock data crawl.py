#使用tushare模块获取“海通证券”（600837）的股票数据，时间从2021.1.1到2021.4.4
import tushare as ts
import pandas as pd
# 设置最大列数，避免只显示部分列
pd.set_option('display.max_columns', 1000)
# 设置最大行数，避免只显示部分行数据
# pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)
# 设置每列最大宽度，避免属性值或列名显示不全
pd.set_option('display.max_colwidth',1000)
 
 
token = '' # 设置tocken
pro = ts.pro_api(token) # 初始化pro接口
# 获取数据
df_gldq = pro.daily(ts_code='000651.sz', start_date='20210101', end_date='20210404')
# 打印数据
print(df_gldq)