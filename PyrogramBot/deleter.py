import asyncio
from pyrogram import Client
from pyrogram.errors.exceptions.forbidden_403 import ChatAdminRequired, UserPrivacyRestricted, UserNotMutualContact
from pyrogram.errors.exceptions.bad_request_400 import UserIdInvalid, PeerFlood, UsernameNotOccupied, PeerIdInvalid, UserAlreadyParticipant, UsernameInvalid, InputUserDeactivated, ChatAdminRequired, ChannelInvalid
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import ChatPermissions
# from highlightning_ids import hids
import time
import logging
from random import choices

main_acc = Client(
	'main_acc', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e')

@main_acc.on_message()
async def my_handler(client, message):
	await main_acc.delete_messages(-1001683047590, message.message_id)

main_acc.run()