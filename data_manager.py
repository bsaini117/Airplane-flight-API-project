import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a5b9f38df3cc01445d54b5e990cb5e1d/flightDealsProgram"

class DataManager:

    def __init__(self):
        self.user_flight_Data = {}

    #This class is responsible for talking to the Google Sheet.
    def retrieve_user_flight_Data(self):
        sheety_response = requests.get(url=f"{SHEETY_ENDPOINT}/prices")
        sheety_response.raise_for_status()
        data = sheety_response.json()
        self.user_flight_Data = data["prices"]

        return self.user_flight_Data

    def populate_IATA_codes(self):

        for city in self.user_flight_Data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url =f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/users")
        response.raise_for_status()
        data = response.json()["users"]
        return data













