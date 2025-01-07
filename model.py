
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy

# Load the data
try:
  df = pd.read_csv('Cotton.csv')
except FileNotFoundError:
  print("Error: Please upload the file.")
  exit()

# Prepare the data
# df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year

years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]

# tracker = 0
# Create and train the model
for country in df['Countries'].unique():

    country_data = df[df['Countries'] == country]

    prices = country_data[years].values.flatten()

    X = country_data[years].columns.astype(int).values.reshape(-1, 1)

    model = LinearRegression()

    model.fit(X, prices)

    # Predict for the next 5 years
future_years = list(range(2024, 2029))
    # predicted_data = np.array()
future_X = pd.DataFrame({'Year': future_years})
predictions = model.predict(future_X)
    
counter = 0
for i in future_years:
    predicted = pd.DataFrame({str(i): [predictions[counter]]})
    df = pd.concat([df,predicted], axis = 1)
    counter += 1
    #print(f"\nPredictions for {country}:")
    
    #for year, price in zip(future_years, predictions):
      #print(f"Year {year}: {price:.2f}")

print(df)

    
    #print(f"\nPredictions for {country}:")
    #for year, price in zip(future_years, predictions):
      #print(f"Year {year}: {price:.2f}")

    # tracker += 1






