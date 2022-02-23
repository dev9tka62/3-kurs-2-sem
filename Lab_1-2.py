# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

import re, os

this_script_dir = __file__.replace(os.path.basename(__file__), '') #get asb path to the dir where this script is situated

def parse_sh_cdp_neighbors(command_output):
  hostname = re.search('(\w+)>', command_output)[1]
  cdp_neighbors = {hostname:{}}
  cdp_data = re.findall('(\S+)\s+(\w+ \d+/\d+)\s+(\d+)\s+([RSI ]+?)\s+(\S+)\s+(\w+ \S+)', command_output)

  for line in cdp_data:
    dev_id = line[0]
    local_int = line[1]
    # holdtime = line[2]
    # capability = line[3]
    # platform = line[4]
    port_id = line[5]
    cdp_neighbors[hostname].update({local_int:{dev_id:port_id}})

  return cdp_neighbors

file_name = '{}{}sh_cdp_n_sw1.txt'.format(this_script_dir, '/')
sh_cdp_data = ''
with open(file_name, 'r') as f:
      sh_cdp_data = f.read()

print(parse_sh_cdp_neighbors(sh_cdp_data))