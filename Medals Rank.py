import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# Assuming the CSV file has columns: 'Country', 'Gold', 'Silver', 'Bronze', 'Total'
file_path = 'medals.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Sort the data by the 'Total' column in descending order and select the top 10 countries
top_10_countries = data.sort_values(by='Total', ascending=False).head(10)

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries['Country'], top_10_countries['Total'], color='gold')

# Add labels and title
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Medals', fontsize=12)
plt.title('Top 10 Countries by Total Medals', fontsize=16)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()
