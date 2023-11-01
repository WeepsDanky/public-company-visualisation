# classify the news articles in financialnews.json using openai api gpt-3.5-turbo-0613 
import openai
import json
import pandas as pd
import csv
import time
import os
import dotenv
 
# read the json file
with open('financialnews.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# select the id and headlines from the json file
news_headlines = [{"id": item["id"], "headline": item["headline"]} for item in data]
print('news_headlines loaded!')
# print(news_headlines)

# read the api key
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_headlines(info): 
    # classify the headlines using openai api
    prompt = f'Classify the following headlines into 3 categories: 0, 1, 2. The categories are: 0: Stock Market 1: Economic and political news 2: Others. The headlines are: {info}. Deliver your response in a json array with the following keys: id, output, and a short explanation no more than 10 words. For example,"id": 1, "output": 0, "explanation": "The headline is about economic news.". '

    # print(prompt)
    print('prompting...')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant!"}, 
            {"role": "user", "content": prompt}
        ],
    )
    print('prompted!')
    # print(response)
    def format_response(text): 
        # format the response from openai api - delete \ and \n 
        text = text.replace('\\', '')
        text = text.replace('\n', '')
        return text
    
    formatted_response = format_response(response.choices[0].message.content)
    with open('openai_response.json', 'w') as json_file:
        json.dump(formatted_response, json_file, ensure_ascii=False) 
    print('response saved!')
    

def select_news_stock(filepath, news_type): 
    # select the headlines that are about stock market
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    data = json.loads(data)
    print('data loaded!')
    stock_headlines = []
    for item in data:
        if item["output"] == news_type:
            stock_headlines.append(item)
    print(stock_headlines)
    return stock_headlines 


if __name__ == "__main__":
    # classify_headlines(news_headlines)
    with open('data/stock_url.json', 'w', encoding='utf-8') as json_file:
        json.dump(select_news_stock('openai_response.json', 0), json_file, ensure_ascii=False)

""" 
- [x] classify the news articles in financialnews.json using openai api gpt-3.5-turbo-0613
- [x] select the news articles that are about stock market 
- [] scrape and write the selected news articles to a json file
- [] analyse the selected news articles and write a prompt template for any queries (e.g. langchain) 
- [] database design and setup
 """