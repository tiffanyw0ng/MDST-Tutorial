import numpy as np  # Correct alias for numpy
import pandas as pd
import matplotlib.pyplot as plt  # Correct module from matplotlib

# Load the CSV file
data = pd.read_csv('../data/states_edu.csv')

# Optional: Display the first few rows
print(data.head())
plt.scatter(df['STATE_REVENUE_PER_STUDENT'], df['AVG_MATH_8_SCORE'])
plt.xlabel('STATE_REVENUE_PER_STUDENT')
plt.ylabel('AVG_MATH_8_SCORE')
plt.title('Relationship between STATE_REVENUE_PER_STUDENT and AVG_MATH_8_SCORE')
plt.show()

