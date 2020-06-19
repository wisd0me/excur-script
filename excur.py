#!/usr/bin/python3
import argparse
import requests
import datetime
from bs4 import BeautifulSoup

def excur_get_data(city):
    try:
        answer = requests.get('https://excur.ru/' + city)
    except:
        print('excur: request failed')
        raise

    return answer

def excur_get(what, data):
    try:
        soup = BeautifulSoup(data.text, 'lxml')
    except:
        print('excur: parser init failed')
        raise

    for td in soup.find_all('td'):
        try:
            attr = td.attrs['title']
            if attr == what:
                try:
                    span = td.find('span')
                    return span.text
                except:
                    pass
        except:
            pass

    return '--'

def excur_usd_best_buy_get(data):
    try:
        value = excur_get('Выгодная продажа Доллара США', data)
        return value
    except:
        raise

def excur_usd_best_sell_get(data):
    try:
        value = excur_get('Выгодная покупка Доллара США', data)
        return value
    except:
        raise

def excur_euro_best_buy_get(data):
    try:
        value = excur_get('Выгодная продажа Евро', data)
        return value
    except:
        raise

def excur_euro_best_sell_get(data):
    try:
        value = excur_get('Выгодная покупка Евро', data)
        return value
    except:
        raise

def print_rate(args):
    now = datetime.datetime.now() 
    print(now.strftime("Дата: %d.%m.%Y; Время: %H:%M"))

    try:
        data = excur_get_data(args.city)
    except:
        return

    print('Продать Доллар США : ' + excur_usd_best_buy_get(data))
    print('Купить Доллар США  : ' + excur_usd_best_sell_get(data))

    print('Продать Евро       : ' + excur_euro_best_buy_get(data))
    print('Купить Евро        : ' + excur_euro_best_sell_get(data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Excur check")
    parser.add_argument('-c', '--city', default='Novosibirsk')
    args = parser.parse_args()

    print_rate(args)
