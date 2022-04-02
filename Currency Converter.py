# A python script that converts one currency into some other user chosen currency.

from unittest import result
from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter The Amount You Want To Convert\n"))
from_currency = input("From\n").upper()
to_currency = input("To\n").upper()
print(from_currency, "To", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
