from geopy.geocoders import Nominatim

# Initialize geocoder
geolocator = Nominatim(user_agent="city_locator")

def get_city_coordinates(city_name):
    try:
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            return "City not found."
    except Exception as e:
        return str(e)

# AI Agent Simulation
if __name__ == "__main__":
    print("Welcome! You can ask for coordinates of any city. Type exit to quit.")
    while True:
        city = input("Enter city name (or type exit to quit): ")
        if city.lower() == "exit":
            print("Exiting the agent. Goodbye!")
            break
        coordinates = get_city_coordinates(city)
        print("Coordinates: ", coordinates)
