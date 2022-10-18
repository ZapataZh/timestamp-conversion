import time
import pandas as pd
import numpy as np

input_filename = 'catalog.csv'
data = pd.read_csv(input_filename)
tt = np.zeros((len(data), 1))

for i in range(0, len(data)):
    t = data.t[i].replace('T', ' ')[:-4]  # 通过pandas.replace()函数将T转换为空格;[:-4]去掉秒后的小数点部分;转换格式为："%Y-%m-%d %H:%M:%S"
    # 转换成时间数组
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")  # 将其转换为时间数组
    timestamp = time.mktime(timeArray)  # 转换为时间戳
    tt[i] = timestamp

data.insert(loc=len(data.columns), column='tt', value=tt)
df = data.to_csv('out_' + input_filename, index=False)
print('Conversion completed!')
