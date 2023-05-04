#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager



ORIGIN_CITY_CODE = "LON"
date_from = datetime.now().strftime("%d/%m/%Y")
date_to = (datetime.now() + timedelta(days=30*6)).strftime("%d/%m/%Y")

flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()

sheet_data = data_manager.retrieve_user_flight_Data()


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_Search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_Search.retrieve_flight_search(row['city'])

    data_manager.user_flight_Data = sheet_data
    data_manager.populate_IATA_codes()

for data in sheet_data:
    cheapest_flight = flight_search.retrieve_cheapest_flight(ORIGIN_CITY_CODE, data["iataCode"],date_from, date_to)

    if cheapest_flight is None:
        continue

    if cheapest_flight.price < data["lowestPrice"]:

        user_data = data_manager.get_customer_emails()
        email = [email for email in user_data]
        names = [names for names in user_data]

        notification.send_email(email, message, link)






