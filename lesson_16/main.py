import lesson_16.aval_parser as aval_parser
import lesson_16.private_parser as private_parser
import lesson_16.ukrsib_parser as ukrsib_parser
import lesson_16.obmenka as obmenka_parser


lst = [
    aval_parser.RaiffeisenBankAval(),
    private_parser.PrivateBank(),
    ukrsib_parser.UkrsibBank(),
    obmenka_parser.ObmenkaPoint()
]

for bank in lst:
    name = bank.get_name()
    rates = bank.get_currency_rate()

    print('Bank:', name)
    for rate in rates['rate']:
        print('currency: {currency_name}\tpurchase: {p_rate}\tsale: {s_rate}'.format(
            currency_name=rate.get('currency'),
            p_rate=rate.get('purchase_rate'),
            s_rate=rate.get('sale_rate')
        ))
    print()

