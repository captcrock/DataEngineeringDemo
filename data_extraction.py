import pandas as pd

def extract_airports_data():
    url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
    airports = pd.read_csv(url, header=None)
    return airports

def extract_airlines_data():
    url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
    airlines = pd.read_csv(url, header=None)
    return airlines

def extract_routes_data():
    url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat'
    routes = pd.read_csv(url, header=None)
    return routes
