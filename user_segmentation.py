import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r'C:\Users\abhay\Downloads\Gen AI Product Analyst Assignment\Product Analyst Assignment Dataset.xlsx'
data = pd.read_excel(file_path, sheet_name='Dataset')

# Define thresholds for categorizing users
threshold_core = 20
threshold_power = 50

# Count activities by user
user_activity_counts = data['user_email'].value_counts()

# Create a DataFrame for user counts
user_data = pd.DataFrame(user_activity_counts).reset_index()
user_data.columns = ['user_email', 'Usage_Count']

# Categorize users
user_data['User Category'] = 'Casual'
user_data.loc[user_data['Usage_Count'] >= threshold_core, 'User Category'] = 'Core'
user_data.loc[user_data['Usage_Count'] >= threshold_power, 'User Category'] = 'Power'

# Calculate proportions
user_counts = user_data['User Category'].value_counts()
total_users = len(user_data)
user_proportions = (user_counts / total_users) * 100

# Plot the pie chart
labels = user_proportions.index
sizes = user_proportions.values

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('User Segmentation')
plt.savefig('User_Segmentation_Pie_Chart.png')  # Adjust the path as needed
plt.show()
