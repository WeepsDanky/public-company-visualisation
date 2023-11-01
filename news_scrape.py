import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import json 


# inheriting from the scrapy.Spider class
class MySpider(scrapy.Spider):
    name = "news_spider"  # name for our web scrawler

    def start_requests(self):
        urls = ['https://www.cnbc.com/finance/']   #target url for scraping
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        # user-agent argument is used so that website cannot classify the request as scraping and block it
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        headlines = response.xpath('//a[@class="Card-title"]/text()').extract()   #change it as per your use
        url = response.xpath('//a[@class="Card-title"]/@href').extract()
        print(url)

        data_list = []
        id = 0
        
        for headline, url in zip(headlines, url):
            id += 1
            data_list.append({"id": id , "headline": headline, "url": url, "tag": 0})

        print('XXXXX', data_list)
        # Write data to a JSON file
        with open('financialnews.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False)


process = CrawlerProcess()
process.crawl(MySpider)
process.start() 

