import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Generate 100 random data points
y = 4 + 3 * X + np.random.rand(100, 1)  # Linear relationship with some noise

# Create a linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# Plot the data and the linear regression line
plt.scatter(X, y, label='Data Points')
plt.plot(X_new, y_pred, 'r-', label='Linear Regression Line', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Example')
plt.show()
