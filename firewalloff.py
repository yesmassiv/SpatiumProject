"""Модуль использует netsh для отключения брандмауэра"""

import subprocess
import os
import portforwardlib
import time

try:
    def offer():
        print('Отключение advfirewall:')
        subprocess.check_call('netsh.exe advfirewall set publicprofile state off')
except:
    print('Ошибка отключения брандмауэра.')

try:
    def portredirect():
        print('Попытка перенаправить порт...')
        os.popen("netsh interface portproxy add v4tov4 listenport=9090 listenaddress=192.168.1.70 connectport=9090 connectaddress=95.27.183.90")
        print('Успешно!')
except:
    print('Ошибка при перенаправке портов. Перенаправьте вручную.')

try:
    protocol = 'UDP'
    def redirectport(ip):
        result = None
        while result == None:
         #try:
          result = portforwardlib.forwardPort(9090, 9090, None, ip, False, protocol, 0, 'SpatiumBlockNetwor({})'.format(protocol), True)
         #except:
            # pass
          time.sleep(0.3)
except:
    print('Ошибка при перенаправлении портов.')

def close_port(ip):
    result = None
    while result == None:
        try:
            result = portforwardlib.forwardPort(9090, 9090, None, ip, False, protocol, 1,
                                                'SpatiumBlockNetwor({})'.format(protocol), False)
            print(result)
        except Exception as e:
            print(e)
            pass
        time.sleep(0.3)