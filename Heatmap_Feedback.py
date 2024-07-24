import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the provided Excel file
file_path = 'C:/Users/abhay/Downloads/Gen AI Product Analyst Assignment/Product Analyst Assignment Dataset.xlsx'
data = pd.read_excel(file_path, sheet_name='Dataset')

# Verify the column names
print(data.columns)

# Use 'question' as the index and 'feedback_sentiment' as the columns
feedback_data = data.pivot_table(index='question', columns='feedback_sentiment', aggfunc='size', fill_value=0)

# Create a larger figure
plt.figure(figsize=(16, 12))  # Adjusted size to fit better

# Create a smaller axis on the large figure
ax = plt.gca()
sns.heatmap(feedback_data, annot=True, cmap='coolwarm', linewidths=.5, fmt='d', annot_kws={"size": 8}, ax=ax)  # Adjust annotation size
plt.title('Feedback Sentiment by Question', fontsize=18)  # Adjust title font size
plt.xlabel('Feedback Sentiment', fontsize=14)  # Adjust x-axis label font size
plt.ylabel('Question', fontsize=14)  # Adjust y-axis label font size
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate x-axis labels and adjust font size
plt.yticks(rotation=0, fontsize=10)  # Ensure y-axis labels are horizontal and adjust font size

# Adjust the padding around the plot
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)  # Reduced right padding

# Adjust the file path to be compatible with Windows
output_path = 'C:/Users/abhay/Downloads/Gen AI Product Analyst Assignment/Feedback_Heatmap.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0.5)  # Adjust padding
plt.show()
