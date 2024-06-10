import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the compliance report
report_path = os.path.join('data', 'compliance_report.csv')

# Load the compliance report into a DataFrame
df = pd.read_csv(report_path)

# Print the first few rows of the DataFrame for a quick preview
print("First few rows of the compliance report:")
print(df.head())

# Get a summary of the issues by severity
severity_summary = df['issue_severity'].value_counts()
print("\nSummary of issues by severity:")
print(severity_summary)

# Plot the summary of issues by severity using a bar chart
severity_summary.plot(kind='bar', color=['green', 'orange', 'red'])
plt.xlabel('Severity')  # Label for the x-axis
plt.ylabel('Count')  # Label for the y-axis
plt.title('Number of Issues by Severity Level')  # Title of the plot
plt.show()  # Display the plot
