import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


class covid19:
	def __init__(self):
		self.req = requests.Session()
		self.bs = bs
		self.url = 'https://www.worldometers.info/coronavirus/country/{}/'

	def corona(self, country):
		try:
			r = self.req.get(self.url.format(country))
			soup = self.bs(r.content, 'html.parser')
			b = soup.findAll('span')
			for x in b:
				c = x.getText()
				corona.append(c)

			del corona[0:4]
			last_update = datetime.now()
			tgl = last_update.strftime('%d %m %Y')
			print('\nTerakhir update : %a' % tgl)
			print('\nTotal Cases\t: %s ' % corona[0])
			print('Deaths\t\t: %s ' % corona[1])
			print('Recovered\t: %s ' % corona[2])
		except IndexError:
			print('Negara tidak ditemukan')

	def source(self):
		self.source = 'https://www.worldometers.info/'
		print('\nSource : %s ' % self.source)


if __name__=="__main__":
	corona=[]
	main=covid19()
	country = input('country : ')
	if country:
		main.corona(country)
		main.source()
