# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from models import Product, db_connect, create_table

class SaveNkimPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        product = Product()
        product.name = item["product_name"]
        product.code = item["product_code"]
        product.price_nkim = item["price"]
        #product.price_tiki = "0"

        try:
            session.add(product)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class DuplicatesPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        exist_product = session.query(Product).filter_by(code = item["product_code"]).first()
        if exist_product is not None:
            exist_product.price_nkim = item["price"]
            session.commit()
            raise DropItem("Update item: %s" % item["product_code"])
            session.close()
        else:
            return item
            session.close()