# Bitcoin Price Prediction Program

This program is a simple Python script that uses machine learning to predict the future price of Bitcoin. It uses historical Bitcoin price data to train a machine learning model that can make predictions about future prices.

## Getting Started
To get started with this program, you'll need to have Python 3 installed on your computer, as well as a number of Python packages, including:

1. pandas
2. numpy
3. matplotlib
4. scikit-learn
5. jupyter

You can install these packages using pip, the Python package manager. For example:

```
pip install pandas numpy matplotlib scikit-learn jupyter

```

or You can directly install the packages from the requirements file, you can use the following command to install all the packages listed in the file.

```
pip install -r requirements.txt

```

Once you have these packages installed, navigate to the directory where you saved the Python file and the CSV dataset.
Run the Python file by typing python btc_prediction.py in the command prompt or terminal window and pressing Enter.

## Usage
To use the program, simply open the Jupyter notebook btc_price_prediction.ipynb and follow the instructions in the notebook. You will need to provide the path to a CSV file containing historical Bitcoin price data. The program will use this data to train a machine learning model, which can then be used to make predictions about future prices.

The program currently predicts the price of Bitcoin in the next 24 hours and in the next 30 days. You can modify the program to make predictions for different time periods by adjusting the prediction_days variable in the python file.
