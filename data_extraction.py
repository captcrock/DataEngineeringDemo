import pandas as pd

def extract_airports_data():
    """
    Extracts the airports data from the OpenFlights dataset.
    """
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
    airports = pd.read_csv(url, header=None)
    airports.columns = ['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude', 'Timezone', 'DST', 'Tz', 'Type', 'Source']
    return airports

def extract_airlines_data():
    """
    Extracts the airlines data from the OpenFlights dataset.
    """
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat"
    airlines = pd.read_csv(url, header=None)
    airlines.columns = ['Airline ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country', 'Active']
    return airlines

def extract_routes_data():
    """
    Extracts the routes data from the OpenFlights dataset.
    """
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"
    routes = pd.read_csv(url, header=None)
    routes.columns = ['Airline', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport', 'Destination airport ID', 'Codeshare', 'Stops', 'Equipment']
    return routes
