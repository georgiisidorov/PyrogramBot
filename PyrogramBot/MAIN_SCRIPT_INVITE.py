from pyrogram import Client
from inviting_in_chat import invite_in_chat
from highlightning_ids import hids

proxies_list = [
	'2.56.138.205:52119:dpMRtSiL:thzbZALG',
	'94.154.191.224:61693:dpMRtSiL:thzbZALG',
	'92.249.12.245:54008:dpMRtSiL:thzbZALG',
	'92.249.15.223:56103:dpMRtSiL:thzbZALG',
	'45.131.47.227:47188:dpMRtSiL:thzbZALG',
	'194.156.104.125:62767:dpMRtSiL:thzbZALG',
	'194.156.105.67:54641:dpMRtSiL:thzbZALG',
	'46.150.252.8:62267:dpMRtSiL:thzbZALG',
	'46.150.247.29:56979:dpMRtSiL:thzbZALG',
	'46.150.246.180:64739:dpMRtSiL:thzbZALG',
	'46.150.244.205:49623:dpMRtSiL:thzbZALG'
]

acc1 = Client('acc1', api_id='10240368', api_hash='9c399294c31b3cd07a4997f08a4c6935',
					proxy=dict(hostname=proxies_list[0].split(':')[0], port=int(proxies_list[0].split(':')[1]),
									username=proxies_list[0].split(':')[2], password=proxies_list[0].split(':')[3]))
acc2 = Client('acc2', api_id='7900298', api_hash='cc750a7f342bd3944afda3bdebaaf2e5',
					proxy=dict(hostname=proxies_list[0].split(':')[0], port=int(proxies_list[0].split(':')[1]),
									username=proxies_list[0].split(':')[2], password=proxies_list[0].split(':')[3]))
acc3 = Client('acc3', api_id='6340784', api_hash='9d6d7f19eb71589c3d137b16f99f17ec',
					proxy=dict(hostname=proxies_list[1].split(':')[0], port=int(proxies_list[1].split(':')[1]),
									username=proxies_list[1].split(':')[2], password=proxies_list[1].split(':')[3]))
acc4 = Client('acc4', api_id='7800760', api_hash='c95b37aebba5133812a31a1c60737dfe',
					proxy=dict(hostname=proxies_list[1].split(':')[0], port=int(proxies_list[1].split(':')[1]),
									username=proxies_list[1].split(':')[2], password=proxies_list[1].split(':')[3]))
acc5 = Client('acc5', api_id='7846797', api_hash='5110b80b4a5e52efd5a460c8c67052a0',
					proxy=dict(hostname=proxies_list[2].split(':')[0], port=int(proxies_list[2].split(':')[1]),
									username=proxies_list[2].split(':')[2], password=proxies_list[2].split(':')[3]))
acc6 = Client('acc6', api_id='6409043', api_hash='6c13e93f63e73649a49771e7ec3ad2e9',
					proxy=dict(hostname=proxies_list[2].split(':')[0], port=int(proxies_list[2].split(':')[1]),
									username=proxies_list[2].split(':')[2], password=proxies_list[2].split(':')[3]))
acc7 = Client('acc7', api_id='7730612', api_hash='30a0265cd27ef6457d273e3806601dd4',
					proxy=dict(hostname=proxies_list[3].split(':')[0], port=int(proxies_list[3].split(':')[1]),
									username=proxies_list[3].split(':')[2], password=proxies_list[3].split(':')[3]))
acc8 = Client('acc8', api_id='7931373', api_hash='d92839fad3a90489e7e1ebbaad32a808',
					proxy=dict(hostname=proxies_list[3].split(':')[0], port=int(proxies_list[3].split(':')[1]),
									username=proxies_list[3].split(':')[2], password=proxies_list[3].split(':')[3]))
acc9 = Client('acc9', api_id='7137096', api_hash='46b2f68093ee9041953cf4f396bec0bb',
					proxy=dict(hostname=proxies_list[4].split(':')[0], port=int(proxies_list[4].split(':')[1]),
									username=proxies_list[4].split(':')[2], password=proxies_list[4].split(':')[3]))
acc10 = Client('acc10', api_id='7661712', api_hash='09287f029bba929812d9d3448c293bf6',
					proxy=dict(hostname=proxies_list[4].split(':')[0], port=int(proxies_list[4].split(':')[1]),
									username=proxies_list[4].split(':')[2], password=proxies_list[4].split(':')[3]))
acc11 = Client('acc11', api_id='7137365', api_hash='1ee4d3da7338f1e0131dcb3a940df028',
					proxy=dict(hostname=proxies_list[5].split(':')[0], port=int(proxies_list[5].split(':')[1]),
									username=proxies_list[5].split(':')[2], password=proxies_list[5].split(':')[3]))


# вручную добавляем со скрипта tgstat_chats

msg = '''
Ребята, Мария(сами понимаете какая) спалила в сторис секретную библиотеку, откуда все лидеры инфобиза берут информацию для своих дорогих курсов! 

А сам доступ к библиотеке стоит всего 1к !!!

Там вся необходимая инфа по  куче курсов
!!! без воды !!!

Кидаю ссылку, а ваше дело успеть залететь в неё, пока не закрыли доступ : 

https://paywall.pw/rb67a8ybe5xy'''


accs = [acc1, acc2, acc3, acc6, acc7, acc8, acc9, acc10, acc11]

for acc in accs:
	acc.start()


# инвайтинг
invite_in_chat(accs, msg)

for acc in accs:
	acc.start()