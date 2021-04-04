#定义获取多只股票函数：
def get_stocks_data(stocklist,start,end):
    all_data={}
    for code in stocklist:
        all_data[code]=pro.daily(ts_code=code,
                 start_date=start, end_date=end)
    return all_data

#保存本地
def save_data(all_data):
    for code,data in all_data.items():
        data.to_csv('c:/zjy/stock_data/'+code+'.csv',
                     header=True, index=False)

stocklist=list(basic.ts_code)[:15]
start=''
end=''
all_data=get_stocks_data(stocklist,start,end)

all_data['000002.SZ'].tail()

#将数据保存到本地
save_data(all_data)

#读取本地文件夹里所有文件
import os
#文件存储路径
file='c:/zjy/stock_data/'
g=os.walk(file)
filenames=[]
for path,d,filelist in g:
    for filename in filelist:
        filenames.append(os.path.join(filename))
print(filenames)

#将读取的数据文件放入一个字典中
df={}
#从文件名中分离出股票代码
code=[name.split('.')[0] for name in filenames]
for i in range(len(filenames)):
    filename=file+filenames[i]
    df[code[i]]=pd.read_csv(filename)

#查看第一只股票前五行数据
#df[code[0]].head()