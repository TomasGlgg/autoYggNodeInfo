from subprocess import Popen, PIPE

process = Popen('uptime', shell=True, stdout=PIPE)
out = process.communicate()[0].decode().split()
a = out[-3][:-1].replace(',', '.')
b = out[-2][:-1].replace(',', '.')
c = out[-1][:-1].replace(',', '.')

print('Load average:', a, b, c)
