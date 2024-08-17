import pandas as pd
import numpy as np

# Number of data points
num_samples = 100

# Generate random data for the independent variable (X)
X = np.random.uniform(0, 10, num_samples)

# Define the linear relationship: y = 2 * X + 3 + noise
y = 2 * X + 3 + np.random.uniform(-1, 1, num_samples)

# Create a Pandas DataFrame
df = pd.DataFrame({'X': X, 'y': y})

# Specify the CSV file name
csv_file = './random_linear_dataset.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False)

print(f'Dataset saved to {csv_file}')
