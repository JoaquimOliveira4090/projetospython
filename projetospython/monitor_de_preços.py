import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText

def check_price(url, desired_price):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Extrair título e preço (seletores variam por site)
    title = soup.find(id="productTitle").get_text().strip()
    price = float(soup.find(id="priceblock_ourprice").get_text().replace('R$','').replace('.','').replace(',','.'))
    
    if price < desired_price:
        send_alert(title, price, url)

def send_alert(product, price, url):
    # Configurar e-mail (substitua com seus dados)
    sender = 'seuemail@gmail.com'
    password = 'sua_senha'
    receiver = 'emaildestino@example.com'
    
    msg = MIMEText(f"O produto {product} está por R${price:.2f}\n\n{url}")
    msg['Subject'] = f"ALERTA DE PREÇO: {product}"
    msg['From'] = sender
    msg['To'] = receiver
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

import sqlite3

def init_db():
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices
                 (product TEXT, price REAL, date TEXT)''')
    conn.commit()
    conn.close()

def save_price(product, price):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("INSERT INTO prices VALUES (?, ?, datetime('now'))", 
              (product, price))
    conn.commit()
    conn.close()

import schedule
import time

def job():
    check_price("https://www.amazon.com.br/dp/B0CPY3MJ6S/?coliid=I3KSDH2988P96V&colid=2OTAOMYJUPBCF&ref=list_c_wl_lv_cv_lig_dp_it_im&th=1", 200)

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)



from requests.exceptions import RequestException

def safe_check_price(url, desired_price):
    try:
        check_price(url, desired_price)
    except RequestException as e:
        print(f"Erro de conexão: {e}")
    except AttributeError:
        print("Estrutura do site mudou - atualize os seletores")
    except Exception as e:
        print(f"Erro inesperado: {e}")