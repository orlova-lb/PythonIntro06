from bs4 import BeautifulSoup
import requests
import re

from lesson_16.currency import currency


class UkrsibBank:
    __URL = 'https://ukrsibbank.com'
    __NAME = 'UkrSibBank'

    def __get_html(self):
        resp = requests.get(self.__URL)
        return resp.text

    def get_name(self):
        return self.__NAME

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')

        contents = soup.find_all('div', id=re.compile('^NAL*'))
        for line in contents:
            currency_name = None
            for key, value in currency.items():
                if key.lower() in line['id'].lower():
                    currency_name = value
                    break

            if currency_name is None:
                continue

            currency_rate['rate'].append(
                {
                    'currency': currency_name,
                    'purchase_rate': str(round(float(line.find('div', class_='rate__buy').find('p').text.strip('\n').strip()), 2)),
                    'sale_rate': str(round(float(line.find('div', class_='rate__sale').find('p').text.strip('\n').strip()), 2))
                }
            )

        return currency_rate


if __name__ == '__main__':
    bank = UkrSibBank()
    print(bank.get_currency_rate())
