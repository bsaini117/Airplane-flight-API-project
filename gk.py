import requests
from pprint import pprint

tequila_endpoint = "https://api.tequila.kiwi.com/v2/search?"
header = {"apikey": "INSERT API",
          "Content-Type": "json"}

params = {"fly_from":"LON" ,
          "fly_to":"PAR",
          "date_from":"04/03/2023",
          "date_to": "04/06/2023",
          "max_stopovers": "0",
          "flight_type": "round",
          "nights_in_dst_from": "7",
          "nights_in_dst_to": "28",
          "one_for_city": "1",
          "curr": "GBP"}

response = requests.get(url=tequila_endpoint, params=params, headers=header)
response.raise_for_status()
data = response.json()
pprint(data)

