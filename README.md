# Flight Operations Analysis Application

## Description

This application is designed to provide insights into airline operations based on open source flight data. The application extracts data from CSV files, cleans and transforms it, loads it into pandas dataframes, performs analysis, and generates reports. 

## Dependencies

This application requires Python 3.x and the following Python libraries installed:

- pandas
- requests
- matplotlib
- seaborn
- numpy
- smtplib
- email.mime

You can install these dependencies using pip:

```bash
pip install pandas requests matplotlib seaborn numpy secure-smtplib email.mime
```

## Files and Directories

The application consists of the following files:

- `data_extraction.py`: This script contains functions to load data from CSV files into pandas dataframes.
- `data_cleaning.py`: This script contains functions to clean and transform the dataframes.
- `data_loading.py`: This script contains functions to further process and prepare the data for analysis.
- `data_analysis.py`: This script contains functions to perform analysis on the data.
- `report_generation.py`: This script contains functions to generate and email reports based on the analysis results.
- `main.py`: This script orchestrates the whole process by calling functions from the other scripts in the correct order.

## Running the Application

To run the application, navigate to the directory containing the scripts and run the `main.py` script:

```bash
python main.py
```

## Data

The application uses open source flight data from OpenFlights.org. The following CSV files are required:

- `airports.dat`: Contains data about airports.
- `airlines.dat`: Contains data about airlines.
- `routes.dat`: Contains data about airline routes.

These files should be saved in a directory accessible by the scripts. The file paths in the `data_extraction.py` file should be updated to point to the correct location of these files.

## Email Setup

If you want to email the reports, you need to set up an SMTP server. Python's `smtplib` is used for this purpose in the `report_generation.py` file. You need to provide your email server details (like server name, port), as well as your email address and password.

## Reports

The `report_generation.py` script generates plots using matplotlib and seaborn. These plots are displayed on screen. If you want to save these plots as image files, you can use the `savefig` function from matplotlib. For example, after creating a plot you can call `plt.savefig('plot.png')` to save the image.

Please note that these scripts are simplified and might not cover all edge cases or errors that can occur during real-world usage. You might want to add more error handling and logging to make the scripts more robust.
