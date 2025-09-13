import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('housing.csv')

# Feature (X) and Target (y)
X = data[['median_income']]   # must be 2D
y = data['median_house_value']

# Train-test split (optional, here we use full data for simplicity)
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Metrics
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

sklearn_m = model.coef_[0]
sklearn_b = model.intercept_

print(f"Sklearn Linear Regression:")
print(f"Coefficient (m): {model.coef_[0]}")
print(f"Intercept (b): {model.intercept_}")
print(f"MSE: {mse:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")

# Export for manual comparison
# ...existing code...

# Plot
plt.scatter(X, y, color='blue', alpha=0.5, label='Data points')
plt.plot(X, y_pred, color='red', label='Regression line (sklearn)')
plt.legend()
plt.show()
