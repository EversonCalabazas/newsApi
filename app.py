import requests, json, datetime, pandas as pd

today = datetime.datetime.today().date()
today = today.strftime('%Y-%m-%d') 


url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from={today}&'
       'sortBy=popularity&'
       'apiKey=9d7e959fa3a544ae9eb7041aeff4119d')

response = requests.get(url)
items = json.loads(response.content)

data = pd.DataFrame(items['articles'])
content = data.content
date = data.publishedAt

newsDF = pd.concat([date,content], axis=1)
newsDF.index=[''] * len(newsDF)
print(newsDF)