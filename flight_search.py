import requests
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "u0ccWFt5jOLqW6xPo22RxfJHUvBOaeyq"



class FlightSearch:

    def retrieve_flight_search(self, city):

        header = {"apikey": TEQUILA_API_KEY }
        params = {"term": city, "location_types": "city"}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=params)
        response.raise_for_status()
        data = response.json()["locations"]
        IATA_code = data[0]["code"]
        return IATA_code

    def retrieve_cheapest_flight(self, origin_city_code, destination_city_code, date_from, date_to):
        tequila_endpoint = "https://api.tequila.kiwi.com/v2/search?"
        header = {"apikey": "u0ccWFt5jOLqW6xPo22RxfJHUvBOaeyq",
                  "Content-Type": "json"}

        params = {"fly_from": origin_city_code,
                  "fly_to": destination_city_code,
                  "date_from": date_from,
                  "date_to": date_to,
                  "max_stopovers": "0",
                  "flight_type": "round",
                  "nights_in_dst_from": "7",
                  "nights_in_dst_to": "28",
                  "one_for_city": "1",
                  "curr": "GBP"}

        response = requests.get(url=tequila_endpoint, params=params, headers=header)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for one way {destination_city_code} ")
            try:
                params["max_stopovers"] = 1
                data = response.json()["data"][0]

            except IndexError:
                print(f"No flights found for two way {destination_city_code} ")
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"])

                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data








