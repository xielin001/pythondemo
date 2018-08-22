'''
Created on 2018年4月23日

@author: xielin
'''
import psutil
#方法一

for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)
      
#方法二
pids = psutil.pids()
count = 0
for pid in pids:
    count += 1
    p = psutil.Process(pid)
    print("pid-%d,pidname-%s"%(pid,p.name()))
print("共有%d个进程"%count)