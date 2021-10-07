import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
while True:
    number = input("Enter your phone number: ")
    country = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(country, "en") or "Couldn't resolve the country.")

    service = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service, "en") or "Couldn't resolve the carrier.")