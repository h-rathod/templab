import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset directly from GitHub
url = "https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv"
data = pd.read_csv(url)

# Display the first few rows to understand the data
print(data.head())

# Assuming the dataset has 'YearsExperience' and 'Salary' columns
X = data[['Experience Years']]
y = data['Salary']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Print results
print(f"Intercept (β₀): {model.intercept_:.2f}")
print(f"Slope (β₁): {model.coef_[0]:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.4f}")

# Create visualization
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Simple Linear Regression: Experience vs Salary')
plt.legend()
plt.grid(True)
plt.show()

# Equation of the regression line
print(f"Regression Equation: Salary = {model.intercept_:.2f} + {model.coef_[0]:.2f} × YearsExperience")
