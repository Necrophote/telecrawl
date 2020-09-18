from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst

def extract_code(text):
	# get product code
	if text[-4]==' ' or text[-4]=='.':
		text = text[:-4]
	return text.rsplit(' ', 1)[1]

def extract_name(text):
	return text

# remove "d" in price 
def extract_price(text):
	return text[:-1]

class TiviItem(Item):
	product_name = Field(
		input_processor=MapCompose(extract_name),
		output_processor=TakeFirst()
		)

	product_code = Field(
		input_processor=MapCompose(extract_code),
		output_processor=TakeFirst()
		)

	price = Field(
		input_processor=MapCompose(extract_price),
		output_processor=TakeFirst()
		)