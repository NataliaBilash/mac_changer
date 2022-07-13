#!/usr/bin/env python3
import subprocess
import re #для регулярных выражений
# import optparse #можем получать аргументы от пользователя парсить их и использовать

# parser = optparse.OptionParser()
# parser.add_option("-i", "--interface", dest="interface", help="Интерфейс MAC адрес которого будет изменен")
# parser.add_option("-m", "--new_MAC", dest="new_MAC", help="Новый MAC адрес формата XX:XX:XX:XX:XX:XX")
# (options, arguments) = parser.parse_args()

def check_args(interface, new_MAC, pwd):
if not interface:
print("Не указан интерфейс")
elif not new_MAC:
print("Не указан MAC адрес")
elif not pwd:
print("Не верный пароль")
return interface, new_MAC, pwd

def macchager(interface, new_MAC, pwd):
cmd1 = 'ifconfig ' + interface + ' down'
cmd2 = 'ifconfig ' + interface + ' hw ether ' + new_MAC
cmd3 = 'ifconfig ' + interface + ' up'

subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd1), shell=True)
subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd2), shell=True)
subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd3), shell=True)

def get_current_mac(interface): #узнает текущий MAC адрес
ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))

#С помощью регулярныхвыражений отфильтруется ifconfig_result, где расматриваться будет только MAC адрес

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) #где \w буквенно цифровой символ
if mac_address_search_result:
return mac_address_search_result.group(0)
else:
print("Нечитаемый MAC адрес")

# interface = options.interface #enp5s0
# new_MAC = options.new_MAC #00:00:00:00:00:00
pwd = input("Пароль")
interface = input("Интерфейс MAC адрес которого будет изменен")
new_MAC = input("Новый MAC адрес формата XX:XX:XX:XX:XX:XX")
check_args(interface, new_MAC, pwd)
current_mac = get_current_mac(interface)
print("Изначальный MAC адрес: " + str(current_mac))

mac_chager(interface, new_MAC, pwd)

current_mac = get_current_mac(interface)
if current_mac == interface:
print("MAC адрес успешно изменен, новый MAC адрес: ", interface)
else:
print("MAC адрес не был изменен")