import data_extraction
import data_cleaning
import data_loading
import data_analysis
import report_generation

def main():
    # Perform data extraction
    airports = data_extraction.extract_airports_data()
    airlines = data_extraction.extract_airlines_data()
    routes = data_extraction.extract_routes_data()

    # Clean the data
    cleaned_airports = data_cleaning.clean_airports_data(airports)
    cleaned_airlines = data_cleaning.clean_airlines_data(airlines)
    cleaned_routes = data_cleaning.clean_routes_data(routes)

    # Load the data into a database
    data_loading.load_airports_data(cleaned_airports)
    data_loading.load_airlines_data(cleaned_airlines)
    data_loading.load_routes_data(cleaned_routes)

    # Analyze the data
    airport_analysis_results = data_analysis.analyze_airports_data()
    airline_analysis_results = data_analysis.analyze_airlines_data()
    routes_analysis_results = data_analysis.analyze_routes_data()

    # Generate a report
    report_generation.generate_airports_report(airport_analysis_results)
    report_generation.generate_airlines_report(airline_analysis_results)
    report_generation.generate_routes_report(routes_analysis_results)

if __name__ == "__main__":
    main()
