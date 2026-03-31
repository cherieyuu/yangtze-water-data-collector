import scrapy
from lxml import etree
import json
from waterDataScrapy.items import WaterdatascrapyItem
from hashlib import md5

storageList = ["三峡水库", "丹江口水库"]

class MainWater(scrapy.Spider):
    name = "main_water"
    start_urls = [
        "http://www.cjh.com.cn/sqindex.html",
    ]

    def parse(self, response):
        rText = response.text
        rText = rText[rText.find('var sssq = ') + 11 :]
        rText = rText[: rText.find(';')]
        data = json.loads(rText)

        print(data)

        for dataItem in data:
            resItem = WaterdatascrapyItem()
            resItem['_id'] = md5((dataItem.get('stnm') + str(dataItem.get('tm'))).encode('utf-8')).hexdigest()
            resItem['station'] = dataItem.get('stnm')
            resItem['time'] = dataItem.get('tm')
            resItem['water_level'] = dataItem.get('z')
            resItem['flow_rate'] = self.get_flow_rate(dataItem)

            yield resItem

    def get_flow_rate(self, item):
        if item.get('stnm') in storageList:
            return [item.get('q'), item.get('oq')]
        else:
            return item.get('q')