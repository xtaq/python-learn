#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import requests
import re
from bs4 import BeautifulSoup

file_name = 'dglte.txt'
file_content = '--'*30 + '\n'+ '甩甩尾巴内容' + '\n'
file_content += '生成时间'+time.asctime()+'\n'+'--'*30+'\n'+'--'*30+'\n'

def spider():
	global file_content
	url = 'http://trade.dgtle.com'
	source_code = requests.get(url).text
	sc = re.sub('font-size="22"', 'span', source_code)
	sc = re.sub('font', 'span', sc)
	soup = BeautifulSoup(sc)
	list_soup = soup.find_all('div', class_ = 'tradebox')
	for info in list_soup:
		price = info.find('p', class_='tradeprice').contents[1]
		place = info.find('span',{'class': 'y city'}).string.strip()
		title = info.find('p', class_='tradetitle').contents[0]
		title = ''.join(title)
		user = info.find('p', class_='tradeuser').string.strip()
		date = info.find('span', class_='tradedateline').string.strip()
		view = info.find('span', class_='tradeview').string.strip()
		common = info.find('span',class_='tradecommon').string.strip()
		cvi = view + '/' + common + '\n' + '--'*30
		file_content +='价格:%s \n地点:%s\n物品:%s\n用户:%s\n%s\t\t%s\n' % (price, place, title, user, date, cvi)

spider()
f = open(file_name, 'w')
f.write(file_content)
f.close()

