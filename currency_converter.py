
from forex_python.converter import CurrencyRates
c= CurrencyRates()
amount = int(input("Enter the Amount:"))
from_currency = input("From currency:").upper()
To_currency = input("to currency:").upper()
print(from_currency,"to",To_currency,amount)
result = c.convert(from_currency,To_currency,amount)
print("Converted_currency:",result)

