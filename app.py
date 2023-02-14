import requests, json, datetime, pandas as pd
from IPython.display import HTML

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

newsDF = newsDF.to_html()


from email.policy import SMTP
import smtplib
import email.message

corpo_email = f"""
<p>Olá Everson</p>
<p>Email automático</p>
"{newsDF}"
"""

msg = email.message.Message()
msg['Subject'] = "Assunto"
msg['From'] = "everson.esc@gmail.com"
msg['To'] = "everson.esc@gmail.com"
password = 'ezhhrsdurruzrvlo'
msg.add_header('Content-Type','text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()

s.login(msg['From'], password)
s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')
