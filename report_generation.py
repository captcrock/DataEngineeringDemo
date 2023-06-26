import pandas as pd
import sqlite3

conn = sqlite3.connect('flights_data.db')

def generate_flight_operations_report():
    # This SQL query is a placeholder and would need to be adapted to your actual database schema
    query = '''
        SELECT
            Date,
            Route,
            AircraftType,
            COUNT(*) as NumberOfFlights,
            AVG(Delay) as AverageDelay,
            SUM(CASE WHEN Cancelled THEN 1 ELSE 0 END) as NumberOfCancellations
        FROM
            Flights
        GROUP BY
            Date, Route, AircraftType
    '''
    df = pd.read_sql_query(query, conn)
    df.to_csv('flight_operations_report.csv')

def generate_fleet_utilization_report():
    # This SQL query is a placeholder and would need to be adapted to your actual database schema
    query = '''
        SELECT
            Date,
            AircraftType,
            COUNT(*) as NumberOfFlights,
            SUM(FlightHours) as TotalFlightHours,
            SUM(CASE WHEN Maintenance THEN 1 ELSE 0 END) as NumberOfMaintenanceDays
        FROM
            Flights
        GROUP BY
            Date, AircraftType
    '''
    df = pd.read_sql_query(query, conn)
    df.to_csv('fleet_utilization_report.csv')

def generate_passenger_load_factor_report():
    # This SQL query is a placeholder and would need to be adapted to your actual database schema
    query = '''
        SELECT
            Date,
            Route,
            AircraftType,
            AVG(Passengers) as AveragePassengers
        FROM
            Flights
        GROUP BY
            Date, Route, AircraftType
    '''
    df = pd.read_sql_query(query, conn)
    df.to_csv('passenger_load_factor_report.csv')

def generate_fuel_usage_report():
    # This SQL query is a placeholder and would need to be adapted to your actual database schema
    query = '''
        SELECT
            Date,
            Route,
            AircraftType,
            SUM(FuelUsed) as TotalFuelUsed
        FROM
            Flights
        GROUP BY
            Date, Route, AircraftType
    '''
    df = pd.read_sql_query(query, conn)
    df.to_csv('fuel_usage_report.csv')

def generate_maintenance_report():
    # This SQL query is a placeholder and would need to be adapted to your actual database schema
    query = '''
        SELECT
            Date,
            AircraftType,
            COUNT(*) as NumberOfMaintenanceIncidents,
            SUM(Downtime) as TotalDowntime
        FROM
            Maintenance
        GROUP BY
            Date, AircraftType
    '''
    df = pd.read_sql_query(query, conn)
    df.to_csv('maintenance_report.csv')

def generate_reports():
    generate_flight_operations_report()
    generate_fleet_utilization_report()
    generate_passenger_load_factor_report()
    generate_fuel_usage_report()
    generate_maintenance_report()

generate_reports()
