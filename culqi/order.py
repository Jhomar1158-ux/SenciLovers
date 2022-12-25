import requests

url = "https://api.culqi.com/v2/orders"

payload = {
    "amount": 60000,
    "currency_code": "PEN",
    "description": " Venta de polo",
    "order_number": "#id-9999",
    "expiration_date": "1476132639",
    "client_details": {
        "first_name": "Richard",
        "last_name": "Hendricks",
        "email": "richard@piedpiper.com",
        "phone_number": "999999987"
    },
    "confirm": False,
    "metadata": {"dni": "71702999"}
}
headers = {
    "Authorization": "sk_test_AoFECLzV4fvSZiVX",
    "content-type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)