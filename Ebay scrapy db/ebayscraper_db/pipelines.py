# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EbayscraperDbPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()

        # Remove dollar sign from the price
        value = adapter.get('product_price')
        value = value.replace('$', '')
        adapter['product_price'] = value

        return item


import mysql.connector

class SaveToMySQLPipeline:
    def __init__(self):
        self.conn = mysql.connector.Connect(
            host = 'localhost',
            user = 'root',
            password = 'MzScripter@567',
            database = 'products'
        )

        # Create cursor to execute command
        self.cur = self.conn.cursor()

        # Create products table if none exists
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS products(
                         id int NOT NULL auto_increment,
                         product_title varchar(255),
                         product_price DECIMAL,
                         PRIMARY KEY (id)
                         )
                         """)
    
    def process_item(self, item, spider):
        # Define insert statement
        self.cur.execute(""" INSERT INTO products(
                         product_title,
                         product_price) values (
                         %s,
                         %s)
                """, (
                    item['product_title'],
                    item['product_price']
                ))
        
        # Execute insert of data into database
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        # Close cursor & connetion to database
        self.cur.close()
        self.conn.close()
