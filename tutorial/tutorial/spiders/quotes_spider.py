import scrapy
from tutorial.spiders.Models import *
from sqlalchemy.orm import sessionmaker
#engine = create_engine('sqlite:///market.db', echo=True)

class QuotesSpider(scrapy.Spider):
	# this is the name used by scrapy program to access the spider
	name = "quotes"

	def start_requests(self):
		# this gives the list of urls to scrape from 
		urls = [
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			# start a scrapy request 
			yield scrapy.Request(url=url, callback = self.parse)
	# in scrapy.spider class parse is a default callback function for response
	# so no need to explicitly call out parse as above in start_request method 
	def parse(self,response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('saved file %s ' % filename)


class stockmarket(scrapy.Spider):
	name = "stock"
	def start_requests(self):
		yield scrapy.Request(
		'http://nepalstock.com/todaysprice',
		headers={'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linux x86_64; rv:66.0)Gecko/20100101 Firefox/66.0'},
	)

	def parse(self,response):
		Matrix = [[0 for f in range(9)] for l in range(20)]
		Tatrix = [[0 for f in range(9)] for l in range(20)]
		x = response.css("html body div#home-contents.container table.table.table-condensed.table-hover tr td::text").extract()
		stock = []
		for i in x:
			if not "\n" in i:
				if not "S.N." in i:
					stock.append(i)
		z = 0 
		for i in range(20):
			for j in range(9):
				Matrix[i][j] = stock[z]
				Tatrix[i][j] = j 
				z += 1
		session = sessionmaker(bind=engine)
		session = session()
		for row in range(20):
			tup  = tuple(Matrix[row])

			print(tup)
		# here * is used to pass tuple as argument
			session.add(Market(*tup))
			session.commit()

		# page = response.url.split("/")[-2]
		# filename = "stock-%s.html" %page
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)
		# self.log('saved file %s' %filename)
