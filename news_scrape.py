import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import json 


# inheriting from the scrapy.Spider class
class cnbc_title_spider(scrapy.Spider):
    name = "news_spider"  # name for our web scrawler

    def start_requests(self, target_url=['https://www.cnbc.com/finance/']):
        urls = target_url   #target url for scraping
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
            data_list.append({"id": id , "headline": headline, "url": url, "tag": 0, "output": 0, "text": ""})
        # Write data to a JSON file
        with open('data/financialnews.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False)

# class cnbc_text_spider(scrapy.Spider): 
    

# Scrape cnbc news titles
""" process = CrawlerProcess()
process.crawl(cnbc_title_spider, target_url=['https://www.cnbc.com/finance/'])
process.start()   """

# # Scrape cnbc news text 
with open("data/stock_url.json", 'r', encoding='utf-8') as json_file:
    stock_url = json.load(json_file)
    print(stock_url[0])
    process = CrawlerProcess()
    process.crawl(cnbc_text_spider, target_url=stock_url[0])
    process.start()

""" 
- [x] classify the news articles in financialnews.json using openai api gpt-3.5-turbo-0613
- [x] select the news articles that are about stock market 
- [] scrape and write the selected news articles to a json file from stock_url.json - cnbc_text_spider
    - [] try research online about available cnbc/news_website scrapy spiders
- [] analyse the selected news articles and write a prompt template for any queries (e.g. langchain) 
- [] database design and setup
 """