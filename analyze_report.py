import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the compliance report
report_path = os.path.join('data', 'compliance_report.csv')

# Load the compliance report
df = pd.read_csv(report_path)

# Print the first few rows of the dataframe
print("First few rows of the compliance report:")
print(df.head())

# Example: Get a summary of the issues by severity
severity_summary = df['issue_severity'].value_counts()
print("\nSummary of issues by severity:")
print(severity_summary)

# Plot the summary of issues by severity
severity_summary.plot(kind='bar', color=['green', 'orange', 'red'])
plt.xlabel('Severity')
plt.ylabel('Count')
plt.title('Number of Issues by Severity Level')
plt.show()
