import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Test-Exclusive-2051-Multi-Storage/dp/B086KF4FZF/ref=sr_1_1?dchild=1&keywords=s20&qid=1615455723&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    convertedPrice = price[2:8]
    convertedPrice = float(convertedPrice.replace(',', ''))

    if(convertedPrice <= 35000.0):
        send_mail()

    print(convertedPrice)
    print(price.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<EmailId>', '<email App password>')
    subject = 'Price fell down!'
    body = 'check amazon link https://www.amazon.in/Test-Exclusive-2051-Multi-Storage/dp/B086KF4FZF/ref=sr_1_1?dchild=1&keywords=s20&qid=1615455723&sr=8-1'
    msg = f'Subject:{subject} \n\n {body}'

    server.sendmail('<FromEmail>', '<ToEmail', msg)
    print('EMAIL SENT!!!')
    server.quit()


while(True):
    check_price()
    time.sleep(86400) #checks once per day 86,400 sec
