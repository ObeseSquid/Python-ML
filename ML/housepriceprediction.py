import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Given data
data = {
    'RoomSize': [1, 1, 4, 2, 2, 3, 3, 5, 5, 1, 2, 2, 3, 5, 4], 
    'Price': [133, 112, 290, 177, 200, 250, 255, 400, 370, 146, 140, 170, 220, 300, 330]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Splitting the data into features and target
X = df[['RoomSize']]
y = df['Price']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the price for a room size of 6
room_size_input = np.array([[5]])
predicted_price = model.predict(room_size_input)[0]
print(f'Expected price for room size 5: ${predicted_price:.2f}')