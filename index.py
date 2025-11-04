python
import pandas as pd
import matplotlib.pyplot as plt

# Load the real estate dataset
real_estate_data = pd.read_csv('Abu_Dhabi_Real_Estate_Market_Insights.csv')

# Display the first few rows of the dataset
print(real_estate_data.head())

# Plotting property prices across different neighborhoods
neighborhood_prices = real_estate_data.groupby('Neighborhood')['Price_per_Square_Meter'].mean()
neighborhood_prices.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Average Property Prices per Neighborhood')
plt.xlabel('Neighborhood')
plt.ylabel('Average Price per Square Meter (AED)')
plt.show()

# Analyze rental trends
rental_trends = real_estate_data.groupby('Year')['Average_Rental_Yield'].mean()
rental_trends.plot(figsize=(10, 6), color='green')
plt.title('Average Rental Yields Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Rental Yield (%)')
plt.show()

# Visualize transaction volumes
transaction_volumes = real_estate_data.groupby('Year')['Transaction_Volume'].sum()
transaction_volumes.plot(kind='line', figsize=(10, 6), color='orange')
plt.title('Total Transaction Volumes Over the Years')
plt.xlabel('Year')
plt.ylabel('Transaction Volume')
plt.show()
