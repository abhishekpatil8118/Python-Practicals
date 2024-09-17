from forex_python.converter import CurrencyRates
c=CurrencyRates()
doller=c.get_rate('USD','INR')
inp=float(input("Enter Dollers: "))
ruppe=inp*(round(doller,2))
print("Currency in Ruppes: ",ruppe)
