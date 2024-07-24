import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r'C:\Users\abhay\Downloads\Gen AI Product Analyst Assignment\Product Analyst Assignment Dataset.xlsx'
data = pd.read_excel(file_path, sheet_name='Dataset')

# Sample columns assumed for this example
# 'created_at' is the date of user activity
# Convert 'created_at' to datetime format
data['created_at'] = pd.to_datetime(data['created_at'])

# Define the start date for the retention analysis
start_date = data['created_at'].min()

# Calculate the number of days since the start date for each entry
data['days_since_start'] = (data['created_at'] - start_date).dt.days

# Define time periods (e.g., 0, 7, 14, 21, 28 days)
time_periods = [0, 7, 14, 21, 28]

# Create an empty list to store retention rates
retention_rates = []

# Calculate retention rate for each time period
for period in time_periods:
    # Number of unique users who were active at the start
    initial_users = data[data['days_since_start'] == 0]['user_email'].nunique()
    
    # Number of unique users who are still active at the current period
    active_users = data[data['days_since_start'] <= period]['user_email'].nunique()
    
    # Retention rate (percentage)
    retention_rate = (active_users / initial_users) * 100 if initial_users > 0 else 0
    retention_rates.append(retention_rate)

# Plot the retention curve
plt.plot(time_periods, retention_rates, marker='o')
plt.xlabel('Days')
plt.ylabel('Retention Rate (%)')
plt.title('User Retention Over Time')
plt.grid(True)

plt.savefig('Retention_Curve.png')  # Adjust the path as needed
plt.show()
