import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
# Load the data
data = pd.read_csv('SYY.csv')

# Convert date to datetime format
data['Date'] = pd.to_datetime(data['Date'], utc=True)  # convert 'Date' column to datetime type
data.set_index('Date', inplace=True)

# Feature Engineering
data['day_of_week'] = data.index.dayofweek
data['day_of_month'] = data.index.day
data['month_of_year'] = data.index.month
data['quarter_of_year'] = data.index.quarter
data['year'] = data.index.year

# Handling Missing Values
data.fillna(method='ffill', inplace=True)

# Scaling
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Volume']])

# Create a DataFrame with the scaled data
scaled_df = pd.DataFrame(scaled_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index=data.index)

# Prepare the data for LSTM
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 3])  # Close price is the target
    return np.array(X), np.array(Y)

look_back = 60
X, Y = create_dataset(scaled_data, look_back)

# Reshape input to be [samples, time steps, features] which is required for LSTM
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



# Create and fit the LSTM network
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, Y_train, batch_size=1, epochs=1)

# Predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Invert predictions
train_predict = scaler.inverse_transform(np.hstack((train_predict, np.zeros((train_predict.shape[0], 4)))))
test_predict = scaler.inverse_transform(np.hstack((test_predict, np.zeros((test_predict.shape[0], 4)))))

# Evaluate the model
train_score = np.sqrt(np.mean((train_predict[:,0] - Y_train)**2))
test_score = np.sqrt(np.mean((test_predict[:,0] - Y_test)**2))

print(f'Train Score: {train_score:.2f} RMSE')
print(f'Test Score: {test_score:.2f} RMSE')


# Get the last `look_back` days from the data to predict the next month
last_days = scaled_data[-look_back:]

# Create the dataset for prediction
X_predict = np.array([last_days[:, 3]])  # Close price for the last `look_back` days
X_predict = np.reshape(X_predict, (X_predict.shape[0], X_predict.shape[1], 1))

# Predict the next 30 days
future_predictions = []
for _ in range(30):
    prediction = model.predict(X_predict)
    future_predictions.append(prediction[0, 0])
    X_predict = np.append(X_predict[:, 1:, :], prediction.reshape(1, 1, 1), axis=1)

# Invert the predictions
future_predictions = scaler.inverse_transform(np.hstack((np.array(future_predictions).reshape(-1, 1), np.zeros((30, 4)))))

last_day_stock = data[30]
# Print future predictions
print("Future Predictions: ", future_predictions[:, 0])
