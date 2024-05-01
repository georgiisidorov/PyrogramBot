from pyrogram import Client
from pyrogram.errors.exceptions.forbidden_403 import ChatAdminRequired
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from highlightning_ids import hids
import time
import random
import datetime


def send_private(accs, ids, msg):
	while True:
		ids_sent_before = []
		ids_sent_new = []

		file_ids1 = open('ids_sent.txt', 'r')
		for line in file_ids1:
			ids_sent_before.append(int(line))
		file_ids1.close()

		for acc in accs:
			acc.start()
			time.sleep(random.randint(10,15))

		spisok_obschiy = [id for id in ids if id not in ids_sent_before]

		bool_end = True

		for i in range(40):
			for j in range(len(accs)):
				try:
					accs[j].send_message(spisok_obschiy[j + i*len(accs)], msg)
					ids_sent_new.append(spisok_obschiy[j + i*len(accs)])
				except PeerIdInvalid:
					pass
				except IndexError:
					bool_end = False
				if spisok_obschiy[j + i*len(accs)] == spisok_obschiy[-1]:
					break
			if bool_end:
				if spisok_obschiy[j + i * len(accs)] == spisok_obschiy[-1]:
					break
			elif not bool_end:
				break
			time.sleep(random.randint(10,15))

		for acc in accs:
			acc.stop()
			time.sleep(random.randint(10,15))

		file_ids2 = open('ids_sent.txt', 'a')
		for id in ids_sent_new:
			file_ids2.write(str(id)+'\n')
		file_ids2.close()

		while True:
			if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 0:
				break
