# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset
df = pd.read_csv('olympics.csv')

# Data Cleaning
df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill missing Age with median
df['Height'] = df['Height'].fillna(df['Height'].median())  # Fill missing Height with median
df['Weight'] = df['Weight'].fillna(df['Weight'].median())  # Fill missing Weight with median
df['Medal'] = df['Medal'].fillna('No Medal')  # Replace NaN Medals with 'No Medal'
df['Sport'] = df['Sport'].str.strip().str.lower()  # Standardize sport names

# 2. Top 10 Countries in Gymnastics Over Years
gymnastics_data = df[df['Sport'] == 'gymnastics']
top_gymnastics_countries = (
    gymnastics_data.groupby(['Team', 'Year'])['Medal']
    .count()
    .reset_index()
    .groupby('Team')['Medal']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_gymnastics_countries.plot(kind='bar', color='purple')
plt.title('Top 10 Countries in Gymnastics Over Years')
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_gymnastics_countries.png')
plt.show()

# 3. Gender Participation Analysis
gender_distribution = df['Sex'].value_counts()

plt.figure(figsize=(8, 8))
gender_distribution.plot(kind='pie', autopct='%1.1f%%', colors=['#1f77b4', '#ff7f0e'], startangle=90)
plt.title('Gender Distribution in Olympic Participation')
plt.ylabel('')
plt.tight_layout()
plt.savefig('gender_participation.png')
plt.show()

# 4. Sports Count Over Time
sports_count = df.groupby('Year')['Sport'].nunique()

plt.figure(figsize=(12, 6))
sports_count.plot(kind='line', marker='o')
plt.title('Number of Sports Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Sports')
plt.grid()
plt.tight_layout()
plt.savefig('sports_count_over_time.png')
plt.show()

# 5. Age Distribution of Gold Medalists
gold_medals = df[df['Medal'] == 'Gold']
gold_ages = gold_medals['Age']

plt.figure(figsize=(10, 6))
plt.hist(gold_ages, bins=20, color='orange', edgecolor='black')
plt.title('Age Distribution of Gold Medalists')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('age_distribution_gold.png')
plt.show()

# 6. Summer Sports Over Time
summer_sports = df[df['Season'] == 'Summer'].groupby('Year')['Sport'].nunique()

plt.figure(figsize=(12, 6))
summer_sports.plot(kind='line', marker='o', color='blue')
plt.title('Number of Summer Sports Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Sports')
plt.grid()
plt.tight_layout()
plt.savefig('summer_sports_over_time.png')
plt.show()

# 7. Winter Sports Over Time
winter_sports = df[df['Season'] == 'Winter'].groupby('Year')['Sport'].nunique()

plt.figure(figsize=(12, 6))
winter_sports.plot(kind='line', marker='o', color='cyan')
plt.title('Number of Winter Sports Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Sports')
plt.grid()
plt.tight_layout()
plt.savefig('winter_sports_over_time.png')
plt.show()

# 8. Average Height of Male and Female Athletes Over Years
average_height = df.groupby(['Year', 'Sex'])['Height'].mean().unstack()

plt.figure(figsize=(12, 6))
average_height.plot(kind='line', marker='o')
plt.title('Average Height of Male and Female Athletes Over Years')
plt.xlabel('Year')
plt.ylabel('Average Height (cm)')
plt.legend(title='Gender')
plt.grid()
plt.tight_layout()
plt.savefig('average_height_over_years.png')
plt.show()

# 9. Top Performing Athletes in Ice Hockey
recent_olympics = df[df['Year'] >= (df['Year'].max() - 40)]
ice_hockey_data = recent_olympics[recent_olympics['Sport'] == 'ice hockey']
top_athletes = (
    ice_hockey_data.groupby(['Name', 'Sex'])['Medal']
    .value_counts()
    .unstack(fill_value=0)
)
top_athletes = top_athletes.sum(axis=1).nlargest(5)

plt.figure(figsize=(12, 6))
top_athletes.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Top Performing Athletes in Ice Hockey')
plt.xlabel('Athlete')
plt.ylabel('Total Medals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_ice_hockey_athletes.png')
plt.show()

# 10. Analyse India’s Performance in All Olympic Games
india_data = df[df['Team'].str.contains('India', case=False, na=False)]
india_medals = india_data['Medal'].value_counts()

plt.figure(figsize=(10, 6))
india_medals.plot(kind='bar', color=['gold', 'silver', '#cd7f32'])
plt.title('India’s Olympic Performance')
plt.xlabel('Medal Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('india_performance.png')
plt.show()

# Save the Processed Data
df.to_csv('cleaned_olympics.csv', index=False)

print("Analysis completed! Visualizations saved as PNG files, and cleaned data exported.")

