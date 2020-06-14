from bs4 import BeautifulSoup
import requests

from lesson_16.currency import currency


class ObmenkaPoint:
    __URL = 'https://obmenka.od.ua/'
    __NAME = 'ObmenkaPoint'

    def __get_html(self):
        response = requests.get(self.__URL)
        return response.text

    def get_name(self):
        return self.__NAME

    def get_currency_rate(self):
        currency_rate = {
            'rate': []

        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')

        contents = soup.find_all('li', class_='currencies__block')
        for line in contents:
            currency_name = line.find('span', class_='currencies__block-name').text
            if not currency_name.upper().endswith('/UAH') or currency_name[:3].lower() not in currency:
                continue

            currency_name = currency.get(currency_name[:currency_name.find('/')].lower())
            purchase = (
                line.
                    find('span', class_='currencies__block-buy').
                    find('div', class_='currencies__block-num').
                    text.strip()
            )

            sale = (
                line.
                    find('span', class_='currencies__block-sale').
                    find('div', class_='currencies__block-num').
                    text.strip()
            )

            currency_rate['rate'].append(
                {
                    'currency': currency_name,
                    'purchase_rate': str(round(float(purchase), 2)),
                    'sale_rate': str(round(float(sale), 2))
                }
            )

        return currency_rate


if __name__ == '__main__':
    bank = ObmenkaPoint()
    print(bank.get_currency_rate())