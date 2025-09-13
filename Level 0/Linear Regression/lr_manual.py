import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv('housing.csv')

data['median_income'] = (data['median_income'] - data['median_income'].mean()) / data['median_income'].std()
data['median_house_value'] = (data['median_house_value'] - data['median_house_value'].mean()) / data['median_house_value'].std()

# Loss function (MSE)
def loss_function(m, b, x, y):
    total_loss = 0
    N = len(x)
    for i in range(N):
        total_loss += (y.iloc[i] - (m * x.iloc[i] + b)) ** 2
    return total_loss / N

# Gradient Descent
def gradient_descent(m, b, points, l_rate):
    m_grad = 0
    b_grad = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points.iloc[i].median_income
        y = points.iloc[i].median_house_value
        y_pred = m * x + b
        m_grad += -(2/N) * x * (y - y_pred)
        b_grad += -(2/N) * (y - y_pred)
    m -= l_rate * m_grad
    b -= l_rate * b_grad
    return m, b

# Training (manual gradient descent)
m, b = 0, 0
l_rate = 0.01
epochs = 100

for i in range(epochs):
    m, b = gradient_descent(m, b, data, l_rate)
    if i % 100 == 0:   # Print every 100 epochs instead of 500
        loss = loss_function(m, b, data.median_income, data.median_house_value)
        print(f"Epoch {i}: Loss = {loss:.6f}")

print(f"\nManual Gradient Descent parameters: m = {m}, b = {b}")


# Scikit-learn Linear Regression (on normalized data)
X = data[['median_income']]
y = data['median_house_value']
sk_model = LinearRegression()
sk_model.fit(X, y)
sk_m = sk_model.coef_[0]
sk_b = sk_model.intercept_
sk_loss = loss_function(sk_m, sk_b, data.median_income, data.median_house_value)
print(f"Scikit-learn parameters: m = {sk_m}, b = {sk_b}")
print(f"Scikit-learn Loss: {sk_loss:.4f}")

# Plot both regression lines
plt.scatter(data.median_income, data.median_house_value, color='blue', alpha=0.5, label='Data points')
x_vals = np.linspace(data.median_income.min(), data.median_income.max(), 100)
y_manual = m * x_vals + b
y_sklearn = sk_m * x_vals + sk_b
plt.plot(x_vals, y_manual, color='red', label='Manual Regression')
plt.plot(x_vals, y_sklearn, color='green', linestyle='--', label='Sklearn Regression')
plt.legend()
plt.show()
