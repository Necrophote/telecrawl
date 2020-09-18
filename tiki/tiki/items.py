from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst

def extract_code(text):
	return text

def extract_name(text):
	return text

# delete space and linebreak
def extract_price(text):
	text = text.replace('\n','')
	text = text.strip()
	text = text[:-1]
	return text

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