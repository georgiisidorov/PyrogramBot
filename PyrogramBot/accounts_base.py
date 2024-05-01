from pyrogram import Client

f = open('proxies.txt', 'r')
proxies = f.readlines()
proxies_list = []
for proxy in proxies:
	proxies_list.append(proxy.strip('\n'))
f.close()

main_acc = Client(
	'main_acc', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e')

account1 = Client(
	'acc1', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[0].split(':')[0], 
		port=int(proxies_list[0].split(':')[1]),
		username=proxies_list[0].split(':')[2], 
		password=proxies_list[0].split(':')[3]
		)
	)


account2 = Client(
	'acc2', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[0].split(':')[0], 
		port=int(proxies_list[0].split(':')[1]),
		username=proxies_list[0].split(':')[2], 
		password=proxies_list[0].split(':')[3]
		)
	)


account3 = Client(
	'acc3', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[1].split(':')[0], 
		port=int(proxies_list[1].split(':')[1]),
		username=proxies_list[1].split(':')[2], 
		password=proxies_list[1].split(':')[3]
		)
	)


account4 = Client(
	'acc4', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[1].split(':')[0], 
		port=int(proxies_list[1].split(':')[1]),
		username=proxies_list[1].split(':')[2], 
		password=proxies_list[1].split(':')[3]
		)
	)


account5 = Client(
	'acc5', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[2].split(':')[0], 
		port=int(proxies_list[2].split(':')[1]),
		username=proxies_list[2].split(':')[2], 
		password=proxies_list[2].split(':')[3]
		)
	)


account6 = Client(
	'acc6', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[2].split(':')[0], 
		port=int(proxies_list[2].split(':')[1]),
		username=proxies_list[2].split(':')[2], 
		password=proxies_list[2].split(':')[3]
		)
	)


account7 = Client(
	'acc7', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[3].split(':')[0], 
		port=int(proxies_list[3].split(':')[1]),
		username=proxies_list[3].split(':')[2], 
		password=proxies_list[3].split(':')[3]
		)
	)


account8 = Client(
	'acc8', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[3].split(':')[0], 
		port=int(proxies_list[3].split(':')[1]),
		username=proxies_list[3].split(':')[2], 
		password=proxies_list[3].split(':')[3]
		)
	)


account9 = Client(
	'acc9', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[4].split(':')[0], 
		port=int(proxies_list[4].split(':')[1]),
		username=proxies_list[4].split(':')[2], 
		password=proxies_list[4].split(':')[3]
		)
	)


account10 = Client(
	'acc10', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[4].split(':')[0], 
		port=int(proxies_list[4].split(':')[1]),
		username=proxies_list[4].split(':')[2], 
		password=proxies_list[4].split(':')[3]
		)
	)


account11 = Client(
	'acc11', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[5].split(':')[0], 
		port=int(proxies_list[5].split(':')[1]),
		username=proxies_list[5].split(':')[2], 
		password=proxies_list[5].split(':')[3]
		)
	)


account12 = Client(
	'acc12', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[5].split(':')[0], 
		port=int(proxies_list[5].split(':')[1]),
		username=proxies_list[5].split(':')[2], 
		password=proxies_list[5].split(':')[3]
		)
	)


account13 = Client(
	'acc13', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[6].split(':')[0], 
		port=int(proxies_list[6].split(':')[1]),
		username=proxies_list[6].split(':')[2], 
		password=proxies_list[6].split(':')[3]
		)
	)


account14 = Client(
	'acc14', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[6].split(':')[0], 
		port=int(proxies_list[6].split(':')[1]),
		username=proxies_list[6].split(':')[2], 
		password=proxies_list[6].split(':')[3]
		)
	)


account15 = Client(
	'acc15', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[7].split(':')[0], 
		port=int(proxies_list[7].split(':')[1]),
		username=proxies_list[7].split(':')[2], 
		password=proxies_list[7].split(':')[3]
		)
	)


account16 = Client(
	'acc16', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[7].split(':')[0], 
		port=int(proxies_list[7].split(':')[1]),
		username=proxies_list[7].split(':')[2], 
		password=proxies_list[7].split(':')[3]
		)
	)


account17 = Client(
	'acc17', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[8].split(':')[0], 
		port=int(proxies_list[8].split(':')[1]),
		username=proxies_list[8].split(':')[2], 
		password=proxies_list[8].split(':')[3]
		)
	)


account18 = Client(
	'acc18', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[8].split(':')[0], 
		port=int(proxies_list[8].split(':')[1]),
		username=proxies_list[8].split(':')[2], 
		password=proxies_list[8].split(':')[3]
		)
	)


account19 = Client(
	'acc19', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[9].split(':')[0], 
		port=int(proxies_list[9].split(':')[1]),
		username=proxies_list[9].split(':')[2], 
		password=proxies_list[9].split(':')[3]
		)
	)


account20 = Client(
	'acc20', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[9].split(':')[0], 
		port=int(proxies_list[9].split(':')[1]),
		username=proxies_list[9].split(':')[2], 
		password=proxies_list[9].split(':')[3]
		)
	)


account21 = Client(
	'acc21', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[10].split(':')[0], 
		port=int(proxies_list[10].split(':')[1]),
		username=proxies_list[10].split(':')[2], 
		password=proxies_list[10].split(':')[3]
		)
	)


account22 = Client(
	'acc22', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[10].split(':')[0], 
		port=int(proxies_list[10].split(':')[1]),
		username=proxies_list[10].split(':')[2], 
		password=proxies_list[10].split(':')[3]
		)
	)


account23 = Client(
	'acc23', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[11].split(':')[0], 
		port=int(proxies_list[11].split(':')[1]),
		username=proxies_list[11].split(':')[2], 
		password=proxies_list[11].split(':')[3]
		)
	)


account24 = Client(
	'acc24', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[11].split(':')[0], 
		port=int(proxies_list[11].split(':')[1]),
		username=proxies_list[11].split(':')[2], 
		password=proxies_list[11].split(':')[3]
		)
	)


account25 = Client(
	'acc25', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[12].split(':')[0], 
		port=int(proxies_list[12].split(':')[1]),
		username=proxies_list[12].split(':')[2], 
		password=proxies_list[12].split(':')[3]
		)
	)


account26 = Client(
	'acc26', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[12].split(':')[0], 
		port=int(proxies_list[12].split(':')[1]),
		username=proxies_list[12].split(':')[2], 
		password=proxies_list[12].split(':')[3]
		)
	)


account27 = Client(
	'acc27', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[13].split(':')[0], 
		port=int(proxies_list[13].split(':')[1]),
		username=proxies_list[13].split(':')[2], 
		password=proxies_list[13].split(':')[3]
		)
	)


account28 = Client(
	'acc28', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[13].split(':')[0], 
		port=int(proxies_list[13].split(':')[1]),
		username=proxies_list[13].split(':')[2], 
		password=proxies_list[13].split(':')[3]
		)
	)


account29 = Client(
	'acc29', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[14].split(':')[0], 
		port=int(proxies_list[14].split(':')[1]),
		username=proxies_list[14].split(':')[2], 
		password=proxies_list[14].split(':')[3]
		)
	)


account30 = Client(
	'acc30', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[14].split(':')[0], 
		port=int(proxies_list[14].split(':')[1]),
		username=proxies_list[14].split(':')[2], 
		password=proxies_list[14].split(':')[3]
		)
	)


account31 = Client(
	'acc31', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[15].split(':')[0], 
		port=int(proxies_list[15].split(':')[1]),
		username=proxies_list[15].split(':')[2], 
		password=proxies_list[15].split(':')[3]
		)
	)


account32 = Client(
	'acc32', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[15].split(':')[0], 
		port=int(proxies_list[15].split(':')[1]),
		username=proxies_list[15].split(':')[2], 
		password=proxies_list[15].split(':')[3]
		)
	)


account33 = Client(
	'acc33', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[16].split(':')[0], 
		port=int(proxies_list[16].split(':')[1]),
		username=proxies_list[16].split(':')[2], 
		password=proxies_list[16].split(':')[3]
		)
	)


account34 = Client(
	'acc34', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[16].split(':')[0], 
		port=int(proxies_list[16].split(':')[1]),
		username=proxies_list[16].split(':')[2], 
		password=proxies_list[16].split(':')[3]
		)
	)


account35 = Client(
	'acc35', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[17].split(':')[0], 
		port=int(proxies_list[17].split(':')[1]),
		username=proxies_list[17].split(':')[2], 
		password=proxies_list[17].split(':')[3]
		)
	)


account36 = Client(
	'acc36', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[17].split(':')[0], 
		port=int(proxies_list[17].split(':')[1]),
		username=proxies_list[17].split(':')[2], 
		password=proxies_list[17].split(':')[3]
		)
	)


account37 = Client(
	'acc37', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[18].split(':')[0], 
		port=int(proxies_list[18].split(':')[1]),
		username=proxies_list[18].split(':')[2], 
		password=proxies_list[18].split(':')[3]
		)
	)


account38 = Client(
	'acc38', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[18].split(':')[0], 
		port=int(proxies_list[18].split(':')[1]),
		username=proxies_list[18].split(':')[2], 
		password=proxies_list[18].split(':')[3]
		)
	)


account39 = Client(
	'acc39', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[19].split(':')[0], 
		port=int(proxies_list[19].split(':')[1]),
		username=proxies_list[19].split(':')[2], 
		password=proxies_list[19].split(':')[3]
		)
	)


account40 = Client(
	'acc40', 
	api_id='6',
	api_hash='eb06d4abfb49dc3eeb1aeb98ae0f581e', 
	proxy=dict(
		hostname=proxies_list[19].split(':')[0], 
		port=int(proxies_list[19].split(':')[1]),
		username=proxies_list[19].split(':')[2], 
		password=proxies_list[19].split(':')[3]
		)
	)
