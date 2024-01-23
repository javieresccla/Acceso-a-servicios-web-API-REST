import requests

amount = int(input("Introduzca la cantidad que desee convertir: "))
currency_from = input("Introduzca la moneda de esta cantidad en formato ISO 4217: ")
currency_to = input("¿A qué moneda desea convertirlo?: ")

# The API endpoint
url = "https://v6.exchangerate-api.com/v6/18ded058e751f7cc99ce3a9b/pair/"+ currency_from +"/"+ currency_to

# A GET request to the API
response = requests.get(url)

if (response):
    response_json = response.json()

    conversion_rate = response_json["conversion_rate"]

    print(f'La tasa de conversión es de 1 {currency_from} = {conversion_rate} {currency_to}')

    converted_amount = amount * conversion_rate

    print(f'La cantidad introducida equivale a {converted_amount} {currency_to}')

else:
    print(response)
