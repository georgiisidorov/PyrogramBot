from pyrogram import Client
from sending_in_private import send_private
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



target_chats = ["OkVB863Q7p1hMjky", '@kursionline_slavynskiimir', '@ydalenna', '@frilanc', '@freelance_help', '@work_frilans', '@invest_moneycom', '@proffreelancee_chat', '@andreyarbenin2', '@saves_cash_chat', '@freelance_birzha', '@pomogator', '@chatpetra_sineguba', '@piarchato']
target_ids = hids(acc1, target_chats)

msg = ''''''

accs = [acc3, acc4, acc5, acc6, acc7, acc8, acc9, acc10, acc11]
# рассылка в лс
send_private(accs, target_ids, msg)