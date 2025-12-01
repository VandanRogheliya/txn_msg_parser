# Move to root dir for running it
from txn_msg_parser import TextParser, TxnText
import pprint

# PASS
# txt = {
#     "sender": "HDFCBK-S(smsft)",
#     "text": "Sent Rs.437.00\n From HDFC Bank A/C *5232\n To BLINKIT COMMERCE PRIVATE LIMITED\n On 21/10/25\n Ref 113013279023\n Not You?\n Call 18002586161/SMS BLOCK UPI to 7308080808",
#     "date": "2025-10-21 21:08:15",
#     "type": "sms",
# }

# PASS
# txt = {"sender":"SBIUPI-S(smsft)","text":"Dear UPI user A/C X0843 debited by 4116.0 on date 19Oct25 trf to Sowbhagya Trader Refno 529252049436 If not u? call-1800111109 for other services-18001234-SBI","date":"2025-10-19 15:48:13","type":"sms"}

txt = {"sender":"SBIUPI-S(smsft_fi)","text":"Dear UPI user A/C X0843 debited by 42045.0 on date 14Oct25 trf to IKEA ECOM Mahara Refno 528786042431 If not u? call-1800111109 for other services-18001234-SBI","date":"2025-10-14 21:28:50","type":"sms","id":"test-123"}
tt = TxnText()
tt.__dict__.update(txt)
tp = TextParser(accounts=["SBIUPI", "HDFCBK"])

print("tt")
pprint.pp(tt.__dict__)

txn = tp.parse_text(tt)
print("txn")
pprint.pp(txn.__dict__)
