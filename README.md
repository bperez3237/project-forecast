# Project Forecast

Project Forecast is a tool for managing the financial forecast of a project. It takes an imported .xlsx file of a project's financial forecast and exports an updated .xlsx file with the desired changes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have Python 3 and the following packages installed on your system:

-pandas
-xlsxwriter
You can install these packages using the following command:

```python
pip install pandas xlsxwriter
```

### Installing

To install Project Forecast, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/project-forecast.git
```

### Usage

To use Project Forecast, you must have three different tables saved in xlsx files. Billings, Costs, Activities. Enter in the correct file paths to your local machine in the src/data/import_data.py

Then, run the following command in your terminal to cache the data into pickle files:

```python
python src/data/import_data.py
```

Once the data files are populated. Comment out the writer files you want to use from src/app.py and then run the script.

## Contributing

Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
