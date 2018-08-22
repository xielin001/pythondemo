'''
Created on 2018年4月23日

@author: xielin
'''
#查询当前时间，并将其转化为YYYY/MM/DD HH24:MI:SS格式
'''
Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time 模块的 strftime 方法来格式化日期
'''
import time
import calendar

print(time.ctime())
print(time.time())
print(time.localtime())

# 格式化成2016-03-20 11:45:39形式
#题目答案
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
#print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"

#print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

cal = calendar.month(2018, 5)
#print ("以下输出2016年5月份的日历:",cal)
