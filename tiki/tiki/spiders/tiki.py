import scrapy
from scrapy.loader import ItemLoader
from tiki.items import TiviItem

class TikiSpider(scrapy.Spider):

	# crawl from tiki
	name = "tiki"
	allowed_domains = ["tiki.vn"]
	start_urls = {"https://tiki.vn/tivi/c5015"}

	def parse(self, response):
		tks = response.css('div.product-item')

		for tk in tks:
			loader = ItemLoader(item=TiviItem(), selector=tk)
			# crawl product name and code from title attribute
			loader.add_css('product_name', 'a::attr(title)')
			loader.add_css('product_code', 'a::attr(title)')
			# crawl official final price only
			loader.add_css('price', '.final-price::text')
			yield loader.load_item()

		# yield next page
		for a in response.css('li a.next'):
			yield response.follow(a, callback=self.parse)




		#tikitvs = response.css('div.product-item')
		#for tikitv in tikitvs:
		#	yield {
		#		'name': tikitv.css('a::attr(title)').get(),
		#		'price': tikitv.css('.final-price::text').get(),
		#	}
		#for a in response.css('li a.next'):
		#	yield response.follow(a, callback=self.parse)