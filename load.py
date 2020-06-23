'''
Примерный скрипт для вывода средней нагрузки.
'''

from subprocess import Popen, PIPE

process = Popen('uptime', shell=True, stdout=PIPE)
out = process.communicate()[0].decode().split()
avg_1 = out[-3][:-1].replace(',', '.')  # Убираем линюю информацию
avg_5 = out[-2][:-1].replace(',', '.')  # Оставляем только значения
avf_15 = out[-1][:-1].replace(',', '.')

print('Load average:', avg_1, avg_5, avf_15)
