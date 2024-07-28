# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from scrapy.exceptions import DropItem

class APipeline:
    def __init__(self):
        self.con=sqlite3.connect('table1.db')
        self.cur=self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS table1(country TEXT , temp INTEGER)""")
    def process_item(self, item, spider):
        self.cur.execute(""" INSERT OR IGNORE INTO table1 VALUES(?,?)""",(item['country'],item['temp']))
        self.con.commit()
        return item
    

class ColdPipeline:
     def process_item(self, item, spider):
        if int((item['temp'])[:-1]) > 20:
            raise DropItem('very cold')
        return item
        
             
class  BPipeline:
    def __init__(self):
        self.con=sqlite3.connect('unitable.db')
        self.cur=self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS unitable(professor TEXT, position TEXT,email TEXT)""")
    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO unitable VALUES(?,?,?)""",(item['professor'],item['position'],item['email']))
        self.con.commit()
        return item

