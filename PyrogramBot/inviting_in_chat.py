import asyncio
import sys
from pyrogram.errors.exceptions.forbidden_403 import ChatAdminRequired, UserPrivacyRestricted, UserNotMutualContact
from pyrogram.errors.exceptions.bad_request_400 import ChatIdInvalid, ChatInvalid, ChatRestricted, UserIdInvalid, PeerFlood, UsernameNotOccupied, PeerIdInvalid, UserAlreadyParticipant, UsernameInvalid, InputUserDeactivated, ChatAdminRequired, ChannelInvalid
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import ChatPermissions
import time
import logging
from random import choices
from accounts_base import account1, account2, account3, account4, account5, account6, account7, account8, account9, account10, account11, account12, account13, account14, account15, account16, account17, account18, account19, account20, account21, account22, account23, account24, account25, account26, account27, account28, account29
from pyrogram.errors.exceptions.unauthorized_401 import UserDeactivatedBan


logging.basicConfig(filename='logfile_invite_err.log', level=logging.ERROR)


def invite_in_chat(quantity, chats, invite_chatter, accs):
	for acc in accs:
		acc.start()
		print('акк запущен')
	chat_invite_id = accs[0].get_chat(invite_chatter)['id']
	print('взял id')
	for acc in accs:
		try:
			acc.join_chat(invite_chatter)
		except UserAlreadyParticipant:
			pass

	time.sleep(3)

	file = open('invite_chats.txt', 'a')
	members_ids = []
	amount = 0

	for chatter in range(len(chats)):
		time.sleep(150/len(accs))
		if '@' in chats[chatter]:
			try:
				chat_id = accs[chatter%len(accs)].get_chat(chats[chatter])['id']
				time.sleep(3)
				members = accs[chatter%len(accs)].iter_chat_members(chat_id)
				amount += len(members)
				for member in members:
					username = member['user']['username']
					if username is not None:
						members_ids.append(username)

			except ChatAdminRequired as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except ChannelInvalid as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except PeerIdInvalid as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except PeerFlood as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except UsernameNotOccupied as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except UsernameInvalid as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except FloodWait as fl:
				logging.error('флуд '+ str(fl).split('A wait of ')[-1].split(' seconds')[0]+ ' секунд')
				logging.error(fl)
				sys.exit()
		elif 't.me/' in chats[chatter]:
			try:
				accs[chatter%len(accs)].join_chat(chats[chatter])
				time.sleep(3)
				chat_id = accs[chatter%len(accs)].get_chat(chats[chatter])['id']
				time.sleep(3)
				members = accs[chatter%len(accs)].iter_chat_members(chat_id)
				amount += len(members)
				time.sleep(3)
				accs[chatter%len(accs)].leave_chat(chat_id)
				for member in members:
					username = member['user']['username']
					if username is not None:
						members_ids.append(username)
				
			except ChatAdminRequired as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except ChannelInvalid as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except PeerIdInvalid as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except PeerFlood as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			except UsernameNotOccupied as e:
				file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
				file.write(str(e))
			# except UsernameInvalid as e:
			# 	file.write(f'Чат - {chats[chatter]}\nВылетел с ошибкой\n\n')
			# 	file.write(str(e))
			except FloodWait as fl:
				logging.error('флуд '+ str(fl).split('A wait of ')[-1].split(' seconds')[0]+ ' секунд')
				logging.error(fl)
				sys.exit()

	members_ids = list(set(members_ids))

	file.write(f'Общее количество - {amount}\nС юзернеймом и без дублей - {len(members_ids)}\n')
	file.close()
	failed = 0
	added = 0
	if len(members_ids) < 1.5*quantity:
		logging.error('Мало аудитории для удовлетворения этого заказа')

	days = (quantity*20)//50//len(accs)
	if days == 0:
		days = 1
	for k in range(days):
		file = open('invite_chats.txt', 'a')
		for d in range(50):
					
			time.sleep(300)
			for acc in accs:
				if len(members_ids) > 1:
					lst_sliced = members_ids[0]
					members_ids = members_ids[1:]
				elif len(members_ids) == 1:
					lst_sliced = members_ids[0]
					members_ids = []
				elif len(members_ids) == 0:
					break
				try:
					acc.add_chat_members(-1001683047590, lst_sliced)
					added += 1
				except ChatRestricted:
					logging.error('Чат для инвайта сдох')
					sys.exit()
				except UserAlreadyParticipant as e:
					failed += 1
				except UsernameNotOccupied as e:
					failed += 1
				except UsernameInvalid as e:
					failed += 1
				except UserNotMutualContact as e:
					failed += 1
				except InputUserDeactivated as e:
					failed += 1
				except UserPrivacyRestricted as e:
					failed += 1
				except UserIdInvalid as e:
					failed += 1
		file.write(f'Слившихся юзеров - {failed}\nУспешно заинвайченных - {added}\n\n')
		file.close()
		time.sleep(69600)

	for acc in accs:
		acc.stop()


accs = [account1, account2, account3, account4, account5, account6, account9, account10, account11, account23, account27, account28, account29]


# number = (int(input('Стартовый акк: ')) - 1)
# for acc in range(number, len(accs)):
# 	try:
# 		accs[acc].start()
# 		print(f'Аккаунт {acc+1}')
# 	except UserDeactivatedBan:
# 		pass


invite_in_chat(50, ['https://t.me/+PUFu2cXS-spiZmI6'], '@cryptoanalitikvip', accs)









