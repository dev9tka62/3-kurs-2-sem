# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob, re, os, csv

this_script_dir = __file__.replace(os.path.basename(__file__), '') #get asb path to the dir where this script is situated

sh_version_files = glob.glob('{}/sh_vers*'.format(this_script_dir))
# print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(command_output):
  ios = re.search('Version ([^,]+)', command_output)
  image = re.search('image file is \"(.+)\"', command_output)
  uptime = re.search('uptime is (\d+ days, \d+ hours, \d+ minutes)', command_output)
  return (ios[1], image[1], uptime[1])

def write_inventory_to_csv(data_filenames, csv_filename):
  data = [headers]

  for file_name in data_filenames:
    hostname = (re.search('sh_version_(.+)\.txt', file_name))[1]
    sh_version_data = ""
    with open(file_name, 'r') as f:
      sh_version_data = f.read()
    parsed_sh_version = list(parse_sh_version(sh_version_data))
    parsed_sh_version.insert(0, hostname)
    data.append(parsed_sh_version)

  csv_filename = '{}/{}'.format(this_script_dir, csv_filename)
  with open(csv_filename, 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

write_inventory_to_csv(sh_version_files, 'Lab_1-1.csv')