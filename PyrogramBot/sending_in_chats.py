from pyrogram import Client
from pyrogram.errors.exceptions.forbidden_403 import ChatAdminRequired, ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied, MessageIdInvalid, PeerIdInvalid
import time


def send_chat(accs, iter_chat, chats, msg):
	for i in range(iter_chat, len(chats)):
			if chats[i] != '@mari_vakansii' and chats[i] != '@mari_otzyv':
				if '@' in chats[i]:
					accs[i%11].join_chat(chats[i])
					time.sleep(3)
					chat_id = accs[i%11].get_chat(chats[i])['id']
					time.sleep(3)
					try:
						photo = accs[i%11].send_photo(chat_id, photo='photo3.jpg', caption=msg, parse_mode='html')
					except ChatWriteForbidden:
						pass
					time.sleep(3)
					try:
						accs[i%11].forward_messages(539273267, chat_id, photo['message_id'])
					except MessageIdInvalid:
						pass
					time.sleep(3)
					accs[i%11].leave_chat(chat_id)
				elif 'id' in chats[i]:
					pass
					# acc.join_chat(chat[2:])
					# acc.send_photo(chat[2:], photo='photo_1.jpg', caption=msg, parse_mode='html')
					# acc.leave_chat(chat[2:])
				else:
					accs[i%11].join_chat(f't.me/joinchat/{chat}')
					time.sleep(3)
					chat_id = accs[i%11].get_chat(f't.me/joinchat/{chat}')['id']
					time.sleep(3)
					try:
						photo = accs[i%11].send_photo(chat_id, photo='photo3.jpg', caption=msg, parse_mode='html')
					except ChatWriteForbidden:
						pass
					time.sleep(3)
					try:
						accs[i%11].forward_messages(539273267, chat_id, photo['message_id'])
					except MessageIdInvalid:
						pass
					time.sleep(3)
					accs[i%11].leave_chat(chat_id)
			else:
				accs[i%11].join_chat(chats[i])
				time.sleep(3)
				chat_id = accs[i%11].get_chat(chats[i])['id']
				time.sleep(3)
				try:
					photo = accs[i%11].send_photo(chat_id, photo='photo_1.jpg', caption=msg, parse_mode='html')
				except ChatWriteForbidden:
					pass
				time.sleep(3)
				try:
					accs[i%11].forward_messages(539273267, chat_id, photo['message_id'])
				except MessageIdInvalid:
					pass
				time.sleep(3)
				accs[i%11].leave_chat(chat_id)