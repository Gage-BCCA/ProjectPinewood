import requests
from django.conf import settings

def get_etsy_products():
    url = "listing url"
    headers = {"x-api-key": settings.ETSY_API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
        return None