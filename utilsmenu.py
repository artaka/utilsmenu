import requests, json, os, socket, time, random

def ip():
	print('Введите айпи (если хотите пробить свой айпи, ничего не вводите).')
	ip = input('>>> ')
	if ip == '':
		try:
			response = requests.get('https://ipinfo.io/json')
		except:
			print('Произошла ошибка.')
			print('----------')
			main()
	else:
		try:
			response = requests.get('https://ipinfo.io/' + ip + '/json')
		except:
			print('Произошла ошибка.')
			print('----------')
			main()
	r = response.json()
	try:
		try:
			print('[IP] : ' + r['ip'])
		except:
			pass
		try:
			print('[Страна] : ' + r['country'])
		except:
			pass
		try:
			print('[Регион] : ' + r['region'])
		except:
			pass
		try:
			print('[Город] : ' + r['city'])
		except:
			pass
		try:
			print('[Имя устройства] : ' + r['hostname'])
		except:
			pass
		try:
			print('[Местоположение] : ' + r['loc'])
		except:
			pass
		try:
			print('[Провайдер] : ' + r['org'])
		except:
			pass
		try:
			print('[Часовой пояс] : ' + r['timezone'])
		except:
			pass
		try:
			print('[Почтовый индекс] : ' +  r['postal'])
		except:
			pass
	except:
		print('Произошла ошибка.')
	print('----------')
	main()

def bomber():
    clear()
    print("To exit pres CTRL+C")
    bomber = os.system("bomber")
    

def main():
	print('[1] IP пробив')
	print('[2] Запуск SMS-Бомбера')
	print('[0] Выход')
	a = input('>>> ')
	if a == '1':
		ip()
	elif a == '2':
		bomber()
	elif a == '0':
		print('Завершение программы...')
		time.sleep(1)
		exit()
	else:
		print('Неверная команда.')
		print('----------')
		main()



def slowType(text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

def clear():
	if os.sys.platform == 'win32':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    print("\033[31m _    _ _   _ _     __  __ ")
    print("| |  | | | (_) |   |  \/  |       ")
    print("| |  | | |_ _| |___| \  / | ___ _ __  _   _ ")
    print("| |  | | __| | / __| |\/| |/ _ \ '_ \| | | |")
    print("| |__| | |_| | \__ \ |  | |  __/ | | | |_| |")
    print(" \____/ \__|_|_|___/_|  |_|\___|_| |_|\__,_|\n")
    time.sleep(1)
    slowType("\033[32mCreated by artaka tg:@artakagrand", .03)
    print("\033[37m\n")


    

if __name__ == '__main__':
	clear()
	banner()
	main()