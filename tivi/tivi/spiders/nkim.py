import scrapy
from scrapy.loader import ItemLoader
from tivi.items import TiviItem

class QuotesSpider(scrapy.Spider):
	
	# crawl all tivi product from nguyenkim (name, code, price)
	name = "nkim"
	allowed_domains = ["nguyenkim.com"]
	start_urls = {"https://www.nguyenkim.com/tivi-man-hinh-lcd/?sort_by=position&sort_order=desc"}

	def parse(self, response):
		self.logger.info('Parse function called on {}'.format(response.url))
		tvs = response.css('div.nk-new-layout-product-grid')

		for tv in tvs:
			# getting price url
			p = tv.css('.price-now p::text').get()
			if p is None:
				p = '.price-now p span::text'
			else:
				p = '.price-now p::text'
			# load item
			loader = ItemLoader(item=TiviItem(), selector=tv)
			loader.add_css('product_name', '.label span::text')
			loader.add_css('product_code', '.label span::text')
			loader.add_css('price', p)
			yield loader.load_item()

		# yield next page
		for a in response.css('a.btn_next.ty-pagination__next'):
			yield response.follow(a, callback=self.parse)




			#price = tv.css('.price-now p::text').get()
			#if price is None:
			#	price = tv.css('.price-now p span::text').get()
			#yield {
			#	'product_name': tv.css('.label span::text').get(),
			#	'product_id': tv.css('.label span::text').get(),
			#	'price': price,
			#}