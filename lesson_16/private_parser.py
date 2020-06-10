import requests

from lesson_16.currency import currency


class PrivateBank:
    __URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    __NAME = 'PrivateBank'

    def __get_json(self):
        response = requests.get(self.__URL)
        return response.json()

    def get_name(self):
        return self.__NAME

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        json = self.__get_json()
        for line in json:
            if line['ccy'].lower() in currency.keys():
                currency_rate['rate'].append(
                    {
                        'currency': currency.get(line['ccy'].lower()),
                        'purchase_rate': str(round(float(line['buy']), 2)),
                        'sale_rate': str(round(float(line['sale']), 2))
                    }
                )

        return currency_rate


if __name__ == '__main__':
    bank = PrivateBank()
    print(bank.get_currency_rate())