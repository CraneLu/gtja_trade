'''
Created on Jul 8, 2015

@author: yizhang
'''
from gtja.Trade import Trade

import csv
import time

with open("account_info.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        account_name = row[0]
        password = row[1]
        break

print(account_name, password)
trade = Trade(account_name, password)

trade.login()

time.sleep(3)

c_list = trade.get_current_commission()

for c in c_list:
    print(c)

trade.close()
