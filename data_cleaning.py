import pandas as pd

def clean_airports_data(airports):
    """
    Cleans the airports data.
    """
    # Remove any rows with null values
    airports = airports.dropna()

    # Convert IDs to integers
    airports['Airport ID'] = airports['Airport ID'].astype(int)

    # Convert Latitude, Longitude and Altitude to floats
    airports['Latitude'] = airports['Latitude'].astype(float)
    airports['Longitude'] = airports['Longitude'].astype(float)
    airports['Altitude'] = airports['Altitude'].astype(float)

    return airports

def clean_airlines_data(airlines):
    """
    Cleans the airlines data.
    """
    # Remove any rows with null values
    airlines = airlines.dropna()

    # Convert IDs to integers
    airlines['Airline ID'] = airlines['Airline ID'].astype(int)

    # Convert 'Active' to boolean
    airlines['Active'] = airlines['Active'] == 'Y'

    return airlines

def clean_routes_data(routes):
    """
    Cleans the routes data.
    """
    # Remove any rows with null values
    routes = routes.dropna()

    # Convert IDs to integers
    routes['Airline ID'] = routes['Airline ID'].astype(int)

    return routes
