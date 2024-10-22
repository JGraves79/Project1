import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file into a DataFrame
df = pd.read_csv('Electric_Vehicle_Population_Data_Cleaned.csv')

# Group by Type and Model Year, and count the number of occurrences
type_year_counts = df.groupby(['Type', 'Model Year']).size().unstack(fill_value=0)

# Plot the sales trends for each model type by model year
type_year_counts.plot(kind='bar', stacked=True, figsize=(15, 10))
plt.title('Sales Trends by Model Type and Model Year')
plt.xlabel('Model Type')
plt.ylabel('Number of Vehicles')
plt.legend(title='Model Year')
plt.show()

############################################

# Extract relevant columns: Model Year, Range, and Type
df = df[['Model Year', 'Range ', 'Type']]

# Group by Model Year and Type, then calculate the average range for each year and type
average_range_per_year_type = df.groupby(['Model Year', 'Type'])['Range '].mean().unstack()

# Plot the data
plt.figure(figsize=(10, 6))
average_range_per_year_type.plot(kind='bar', stacked=True, color=['skyblue', 'orange'])
plt.title('Average Vehicle Range by Model Year and Type')
plt.xlabel('Model Year')
plt.ylabel('Average Range (miles)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('average_vehicle_range_by_model_year_and_type.png')

# Display the plot
plt.show()

####################Pie Chart 
plt.figure(figsize=(10, 10))
df['Type'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title('Distribution of Vehicle Types')
plt.ylabel('')
plt.show()

#####################

# Extract relevant columns: Model and Price
df = df[['Model', 'Price']]

# Group by Model and calculate the average price for each model
average_price_per_model = df.groupby('Model')['Price'].mean().sort_values()

# Plot the data
plt.figure(figsize=(12, 8))
average_price_per_model.plot(kind='barh', color='lightgreen')
plt.title('Average Price by Vehicle Model')
plt.xlabel('Average Price (USD)')
plt.ylabel('Vehicle Model')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('average_price_by_vehicle_model.png')

# Display the plot
plt.show()