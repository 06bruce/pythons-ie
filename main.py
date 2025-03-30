import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
from trackIt import number  # Assuming 'number' is defined in trackIt.py
import random

try:
    # Verify the number is changing
    print(f"Tracking Phone Number: {number}")

    # Parse the phone number
    pepnumber = phonenumbers.parse(number)
    
    # Get the location description
    location = geocoder.description_for_number(pepnumber, "en").strip()
    print(f"Location: {location}")
    
    # Check if location is empty
    if not location:
        print("Could not determine location from phone number.")
        exit()
    
    # Get the service provider name
    service_provider = carrier.name_for_number(pepnumber, "en")
    print(f"Service Provider: {service_provider}")
    
    # Geocode the location using OpenCage
    key = '52b1a7fd083847c08e4cd8c6946be24d'  # User-provided API key
    geocoder_api = OpenCageGeocode(key)
    
    # Debugging: Print the location query before sending it to OpenCage
    print(f"Querying OpenCage with: {location}")
    
    # Geocode with country hint for better accuracy
    results = geocoder_api.geocode(location, countrycode="rw")  # Use "rw" for Rwanda
    
    # Debugging: Print the full API response
    print(f"OpenCage API Response: {results}")
    
    # Extract latitude and longitude
    if results and len(results) > 0:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Latitude: {lat}, Longitude: {lng}")
    else:
        print("Could not retrieve latitude and longitude. OpenCage may not recognize the location.")

except phonenumbers.NumberParseException as e:
    print(f"Error parsing phone number: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
 