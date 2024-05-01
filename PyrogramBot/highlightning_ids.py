from pyrogram import Client
from pyrogram.errors.exceptions.forbidden_403 import ChatAdminRequired
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
import time


def hids(acc, chat):
	members = []
	members_ids = []

	try:
		if '@' in chat:
			chat_id = acc.get_chat(chat)['id']
			members.extend(acc.iter_chat_members(chat_id))
		elif 'id' in chat:
			pass
			# acc.join_chat(chat[2:])
			# members.extend(acc.iter_chat_members(chat[2:]))
			# acc.leave_chat(chat[2:], delete=True)
		else:
			pass
			# acc.join_chat(f't.me/joinchat/{chat}')
			# chat_id = acc.get_chat(f't.me/joinchat/{chat}')['id']
			# members.extend(acc.iter_chat_members(chat_id))
			# acc.leave_chat(chat_id, delete=True)
	except KeyError:
		pass
	except ValueError:
		pass
	except UsernameNotOccupied:
		pass
	time.sleep(5)


	for member in members:
		members_ids.append(member['user']['id'])

	return list(set(members_ids))