# classify the news articles in financialnews.json using openai api gpt-3.5-turbo-0613 
import openai
import json
import pandas as pd
import csv
import time
import os
import dotenv
 
# read the json file
with open('data/financialnews.json', 'r', encoding='utf-8') as json_file:
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
        max_tokens=2000
    )
    print(response)
    print('Response received!')
    with open('data/openai_response.json', 'w') as json_file:
        json.dump(response['choices'][0]['message']['content'], json_file, ensure_ascii=False) 
    print('response saved!')
    return response['choices'][0]['message']['content']
    

def select_news_stock(filepath, news_type): 
    # select the headlines that are about stock market
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    print('data loaded!')
    stock_headlines = []
    for item in data:
        if item["output"] == news_type:
            stock_headlines.append(item)
    print(stock_headlines)
    return stock_headlines 

if __name__ == "__main__":
    # classify_headlines(news_headlines)
    with open('data/openai_response.json', 'r', encoding='utf-8') as json_file:
        response = json.load(json_file)
    
    id_list = [item["id"] for item in response] 
    print(id_list) 
    # get all the url when id of financialnews.json is in id_list
    with open('data/financialnews.json', 'r', encoding='utf-8') as json_file:
        news = json.load(json_file)
        url_list = [item["url"] for item in news if item["id"] in id_list]
        print(url_list)
        # write the url_list to a json file 
        with open('data/stock_url.json', 'w', encoding='utf-8') as json_file:
            json.dump(url_list, json_file, ensure_ascii=False)
        print('stock url saved!')

""" 
- [x] classify the news articles in financialnews.json using openai api gpt-3.5-turbo-0613
- [x] select the news articles that are about stock market 
- [] scrape and write the selected news articles to a json file
- [] analyse the selected news articles and write a prompt template for any queries (e.g. langchain) 
- [] database design and setup
 """