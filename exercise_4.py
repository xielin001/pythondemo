#4、"May 26 02:00:18 [221.239.47.254] 2005 S1-A-TJQJD.P SHELL/5/CMD:task:vt1 ip:221.239.10.131 user:huawei command:ping -c 20 -s 64 -t 1000 219.150.48.1" 截取这个字符串中的所有ip
'''
正则匹配出ip
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
re.search 扫描整个字符串并返回第一个成功的匹配
re.compile函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用

#简单的匹配给定的字符串是否是ip地址,下面的例子它不是IPv4的地址，但是它满足正则表达式
 3 if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", "272.168,1,1"):
 4     print "IP vaild"
 5 else:
 6     print "IP invaild"
 7 #精确的匹配给定的字符串是否是IP地址
 8 if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", "223.168.1.1"):
 9     print "IP vaild"
10 else:
11     print "IP invaild"
12 #简单的从长文本中提取中提取ip地址
13 string_ip = "is this 289.22.22.22 ip ?
14 result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", string_ip)
15 if result:
16     print result
17 else:
18     print "re cannot find ip"
19 #精确提取IP
20 result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip):
21 if result:
22     print result
23 else:
24     print "re cannot find ip
'''


import re
'''
string_ip = "is this 289.22.22.22 ip ?"
result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", string_ip)
if result:
    print (result)
else:
    print ("re cannot find ip")
'''   
    
   
text ="May 26 02:00:18 [221.239.47.254] 2005 S1-A-TJQJD.P SHELL/5/CMD:task:vt1 ip:221.239.10.131 user:huawei command:ping -c 20 -s 64 -t 1000 219.150.48.1"
#pattern = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")

ip_list = re.findall(r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", text)
if ip_list:
    for ip in ip_list:
        print(ip)#type(ip) == 'str'
else:
    print ("re cannot find ip")


