from bs4 import BeautifulSoup 
import requests
from datetime import date
import pandas as pd
########################################################################################################################################################################
'''WrongCode'''
# print(bsobj.prettify())
# print(bsobj.prettify())
# for news in bsobj.findAll('h1'):
#     print(news.text)
# for link in bsobj.findAll("h3"):	
# 	print ("headline : {}".format(link.text))
	# news.append(head.text.strip())
# for news in bsobj.findAll('p',{'class':'gs-c-promo-summary'}):
# 	print (f"news : {news.text}")	
# for i in bsobj.findAll('p',{'class':'gs-c-promo-summary'}):	
# print(len(bsobj.findAll('a',{'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'})))
#  len(bsobj.findAll('p',{'class':'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary'})))
########################################################################################################################################################################
bcc_url = "https://www.theguardian.com/uk"
print(bcc_url)


html = requests.get(bcc_url)

soup = BeautifulSoup(html.content,'html.parser')


links = []
for head in soup.findAll('div',{'class': 'fc-item__container'}):
    links.append(head.a['href'])
print(len(links))
news = []
headline = []
for link in links:
	html1 = requests.get(link)
	soup1 = BeautifulSoup(html1.content,'html.parser')
	for head in soup1.findAll('main',{'class':'css-1kiwfxx'} , 'h1' ):
		headline.append(soup1.h1.text)
		news.append(head.get_text())

		

	
print(len(headline),len(news),len(links))

data = pd.DataFrame({'headline': headline,'news':news})

print(data)










