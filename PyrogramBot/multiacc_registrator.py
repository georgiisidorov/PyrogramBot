from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
from python3_anticaptcha import ImageToTextTask
import requests
import os
import glob
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from python3_anticaptcha.errors import ReadError
from urllib3.exceptions import NewConnectionError, MaxRetryError
from requests.exceptions import ConnectionError

api_keys = [
'b1182f42A1edf45e690d1be2b6f369e0'
]
api_key_1 = '257AAd7f3d27635255c80e641c972698'
api_key_2 = 'f279A30ce1d1deAbdA4687758df2d06c'
api_key_3 = '0bc48dA6cd482e8d518e4f6396e08266'

with open('proxies.txt') as f:
	proxies = f.readlines()


def getBalance(api_key):
	params = urlencode({'api_key': api_key, 'action': 'getBalance'})
	URL = 'https://api.sms-activate.org/stubs/handler_api.php?' + params
	response = requests.get(URL)
	return response.text


def getNumber(api_key):
	params = urlencode({'api_key': api_key, 'action': 'getNumber', 'service': 'uu', 'country': '0'})
	URL = 'https://sms-activate.org/stubs/handler_api.php?' + params
	response = requests.get(URL)
	return response.text


def setStatus(api_key, id, status):
	params = urlencode({'api_key': api_key, 'action': 'setStatus', 'status': str(status), 'id': id})
	URL = 'https://api.sms-activate.org/stubs/handler_api.php?' + params
	response = requests.get(URL)
	return response.text


def getStatus(api_key, id):
	params = urlencode({'api_key': api_key, 'action': 'getStatus', 'id': id})
	URL = 'https://api.sms-activate.org/stubs/handler_api.php?' + params
	response = requests.get(URL)
	return response.text


def new_acc(api_key, id, number, acc_number):
	setStatus(api_key, id, 1)
	code = ''
	for i in range(6):
		time.sleep(15)
		status = getStatus(api_key, id)
		if 'STATUS_OK' in status:
			code = status.split(':')[1]
			print(code)
			break
		time.sleep(15)
	if code == '':
		setStatus(api_key, id, 8)
		print('Код не получен. Регистрация отменена')
		time.sleep(3)
	else:
		time.sleep(2)
		setStatus(api_key, id, 6)
		current_time = time.strftime("%H:%M:%S", time.gmtime())
		print(f'\nАккаунт {acc_number} зарегистрирован в {current_time}\n')
		time.sleep(3)
		acc_number += 1
		return acc_number


def main(amount):
	number_fallen = 0
	counter_fallen = 0
	api_key_i = 0
	acc_number = 1
	finish_number = acc_number + amount
	while acc_number != finish_number:
		try:
			text = getNumber(api_keys[api_key_i])
			if 'ACCESS_NUMBER' in text:
				response_list = text.split(':')
				id, number = response_list[1], response_list[2]
				print(number)
				print(proxies[(acc_number-1)//2])
				wbc = new_acc(api_keys[api_key_i], id, number)
				if wbc is None:
					counter_fallen += 1
				else:
					counter_fallen = 0
			if 'NO_BALANCE' in text:
				counter_fallen = 2
			if 'BANNED' in text:
				counter_fallen = 2
			if counter_fallen == 2:
				counter_fallen = 0
				number_fallen += 2
				if number_fallen != 2*len(api_keys):
					api_key_i += 1
				else:
					api_key_i = 0
		except IndexError:
			api_key_i = 0
		except TimeoutError:
			pass
		except NewConnectionError:
			pass
		except MaxRetryError:
			pass
		except ConnectionError:
			pass
		except WebDriverException:
			pass



amount = int(input('Кол-во аккаунтов, которое нужно зарегистрировать: '))
for i in range(len(api_keys)):
	print(f'Баланс {i+1}го SmsActivate акка: ' + getBalance(api_keys[i]).split(':')[1] + '₽')

# main(amount)
