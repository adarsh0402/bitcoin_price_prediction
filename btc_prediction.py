import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the Bitcoin price data from a CSV file
df = pd.read_csv('bitcoin_price.csv')

# Convert the date column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Set the date column as the index
df.set_index('date', inplace=True)

# Compute the logarithmic returns of the Bitcoin price
df['log_returns'] = np.log(df['price']) - np.log(df['price'].shift(1))

# Compute the rolling mean and standard deviation of the logarithmic returns
df['rolling_mean'] = df['log_returns'].rolling(window=30).mean()
df['rolling_std'] = df['log_returns'].rolling(window=30).std()

# Drop the first 30 rows, which have missing rolling statistics
df = df.dropna()

# Split the data into training and testing sets
train_data = df.iloc[:-30]
test_data = df.iloc[-30:]

# Train a linear regression model on the training data
X_train = train_data[['rolling_mean', 'rolling_std']]
y_train = train_data['price']
model = LinearRegression().fit(X_train, y_train)

# Use the model to predict the Bitcoin price after 30 days
X_test = test_data[['rolling_mean', 'rolling_std']]
predicted_price = model.predict(X_test)[-1]

print("Predicted Bitcoin price after 30 days:", predicted_price)
