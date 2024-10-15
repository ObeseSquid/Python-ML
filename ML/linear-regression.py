import pandas as pd

# House data
data = {
    'House': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    '#Rooms': [1, 1, 4, 2, 2, 3, 3, 5, 5, 1, 2, 2, 3, 5, 4],
    'Price in 100k': [133, 112, 290, 177, 200, 250, 255, 400, 370, 146, 140, 170, 220, 300, 330],
    'x * y': [133, 112, 1160, 354, 400, 750, 765, 2000, 1850, 146, 280, 340, 660, 1500, 1320],
    'x^2': [1, 1, 16, 4, 4, 9, 9, 25, 25, 1, 4, 4, 9, 25, 16],
    'y^2': [17689, 12544, 84100, 31329, 40000, 62500, 65025, 160000, 136900, 21316, 19600, 28900, 48400, 90000, 108900]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Coefficients from linear regression
b0 = 59.08
b1 = 63.495

# Predict price based on number of rooms (linear regression equation y = b0 + b1 * x)
df['Predicted Price in 100k'] = b0 + b1 * df['#Rooms']

# Display the DataFrame with predicted prices
print(df[['House', '#Rooms', 'Price in 100k', 'Predicted Price in 100k']])
