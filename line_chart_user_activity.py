import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided Excel file
file_path = 'C:/Users/abhay/Downloads/Gen AI Product Analyst Assignment/Product Analyst Assignment Dataset.xlsx'
data = pd.read_excel(file_path, sheet_name='Dataset')

# Assume 'created_at' contains datetime information and 'task_status' indicates activity
data['created_at'] = pd.to_datetime(data['created_at'])
data['week'] = data['created_at'].dt.to_period('W').astype(str)

# Group by week and count activities
weekly_activity = data.groupby('week')['task_status'].count()

weeks = weekly_activity.index.tolist()
activity_counts = weekly_activity.values.tolist()

plt.figure(figsize=(12, 6)) 
plt.plot(weeks, activity_counts, marker='o', linestyle='-', color='green')
plt.xlabel('Weeks')
plt.ylabel('Number of Activities')
plt.title('User Activity Over Time')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()  # Adjust the layout to make room for labels

plt.savefig('C:/Users/abhay/Downloads/Gen AI Product Analyst Assignment/User_Activity_Over_Time.png')
plt.show()
