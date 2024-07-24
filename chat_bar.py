import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r'C:\Users\abhay\Downloads\Gen AI Product Analyst Assignment\Product Analyst Assignment Dataset.xlsx'
data = pd.read_excel(file_path, sheet_name='Dataset')

# Sample columns assumed for this example
# 'created_at' is the date of user activity
# Convert 'created_at' to datetime format
data['created_at'] = pd.to_datetime(data['created_at'])

# Define the start date for grouping
start_date = data['created_at'].min()

# Calculate the week number for each entry
data['week_number'] = ((data['created_at'] - start_date).dt.days // 7) + 1

# Group by week number and count the number of queries (assuming each row represents a query)
weekly_usage = data.groupby('week_number').size()

# Define time periods (adjust to your needs)
time_periods = [f'Week {i}' for i in weekly_usage.index]

# Number of queries per week
queries = weekly_usage.values

# Plot the bar chart
plt.bar(time_periods, queries, color='blue')
plt.xlabel('Time Period')
plt.ylabel('Number of Queries')
plt.title('Chat Bar Feature Usage')
plt.grid(axis='y')

plt.savefig('Chat_Bar_Usage_Bar_Chart.png')  # Adjust the path as needed
plt.show()
