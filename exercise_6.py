#-*- coding:utf-8 -*-
import telnetlib
import os
import re
def do_telnet(host,username,password,finish,commands):
     # 连接Telnet服务器  
    tn = telnetlib.Telnet(host, timeout=10)  
    tn.set_debuglevel(0)  
    
    #输入用户名和密码
    tn.read_until('Username:', timeout=None)
    tn.write(username+"\n")
    
    tn.read_until('Password:', timeout=None)
    tn.write(password+"\n")
    
    tn.read_until(finish)  
    result = ''
    for command in commands:
        tn.write('%s\n' % command)
        result += tn.read_until(finish) 
        
    #result = tn.read_all()#如果回显没返回EOF也会卡在这里
    #tn.close()
    return result
#password=aaa,username=aaa

if __name__=='__main__':  
     # 配置选项  
    host = '192.168.6.87' # Telnet服务器IP  
    username = 'aaa'   # 登录用户名  
    password = 'aaa'  # 登录密码  
    finish = '#'      # 命令提示符  
    commands = ["show running-config | inc hostname", "exit"] 
    result = do_telnet(host, username, password, finish, commands)
    pattern = re.compile(r"\nhostname (.+?)\r", flags=0)
    hostname = re.search(pattern, result, flags=0).group().split(' ')[1]
    print(hostname)
