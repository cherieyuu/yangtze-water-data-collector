# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.exceptions import DropItem


class waterDataScrapyPipeline:
    def process_item(self, item, spider):
        return item


def is_blank_value(value):
    return value in (None, "", "-")


def clean_flow_rate(value):
    if isinstance(value, list):
        return [None if is_blank_value(item) else item for item in value]
    return None if is_blank_value(value) else value


class SaveToMongoPipeline:
    def __init__(self, mongo_uri, mongo_db, collection):
        self.momgo_uri = mongo_uri
        self.momgo_db = mongo_db
        self.collection = collection

    @classmethod
    def from_crawler(cls, crawler):
        # Read Mongo config directly from Scrapy settings/env-backed config.
        mongo_uri = crawler.settings.get("MONGO_URI")
        mongo_db = crawler.settings.get("MONGODB_DB")
        collection = crawler.settings.get("COLLECTION_NAME")
        # 返回当前 pipeline 的实例，传入从 settings 中读取的配置
        return cls(
            mongo_uri=mongo_uri,
            mongo_db=mongo_db,
            collection=collection,
        )

    def open_spider(self, spider):
        # 打开 spider 的时候调用一次，可以在这里创建数据的连接
        self.client = pymongo.MongoClient(self.momgo_uri)
        self.db = self.client[self.momgo_db]

    def process_item(self, item, spider):
        # 每一个 item 都会调用这个方法，可以在这里清洗数据，并保存到数据库
        adapter = ItemAdapter(item)
        coll = self.db[self.collection]
        # 使用 ItemAdapter 的 asdict() 方法可以处理嵌套的 item 格式，获取 json 字符串
        doc = adapter.asdict()

        # Skip unusable records so bad placeholder values do not break the API.
        if is_blank_value(doc.get("time")):
            raise DropItem(f"Missing time for station: {doc.get('station')}")

        doc["water_level"] = None if is_blank_value(doc.get("water_level")) else doc.get("water_level")
        doc["flow_rate"] = clean_flow_rate(doc.get("flow_rate"))

        coll.update_one({"_id": doc.get("_id")}, {"$set": doc}, upsert=True)
        return item
  
    def close_spider(self, spider):
        # spider 关闭的时候调用一次，可以在这里关闭数据库连接，释放资源
        self.client.close()
