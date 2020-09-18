# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import literal
from scrapy.exceptions import DropItem
from models import Product, db_connect, create_table

#class SaveTikiPipeline(object):
#    def __init__(self):
#        engine = db_connect()
#        create_table(engine)
#        self.Session = sessionmaker(bind=engine)
#
#    def process_item(self, item, spider):
#        session = self.Session()
#        product = Product()
#        product.name = item["product_name"]
#        product.code = item["product_code"]
#        #product.price_nkim = item["price"]
#        product.price_tiki = item["price"]
#
#        try:
#            session.add(product)
#            session.commit()
#
#        except:
#            session.rollback()
#            raise
#
#        finally:
#            session.close()
#
#        return item

# Compare product code to check if tiki selling the same product as nguyenkim
# If true, update tiki price next to nkim
class DuplicatesPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        exist_product = session.query(Product).filter(literal(item["product_code"]).like('%'+Product.code+'%')).first()
        if exist_product is not None:
            exist_product.price_tiki = item["price"]
            session.commit()
            raise DropItem("Update item: %s" % item["product_code"])
            session.close()
        else:
            raise DropItem()
            session.close()