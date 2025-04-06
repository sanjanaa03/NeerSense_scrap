import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
data['Day'] = pd.Categorical(data['Day']).codes
data['Season'] = pd.Categorical(data['Season']).codes
data['Temperature'] = pd.Categorical(data['Temperature']).codes

X = data[['Previous_Day_Usage','Season','Month','Temperature','Goals_Set_by_User']]
y = data['Water_Consumption']

#80:20 splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
#plotting
plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label='Actual Consumption', marker='o')
plt.plot(y_pred, label='Predicted Consumption', marker='x', linestyle='--')
plt.title('Actual vs Predicted Water Consumption')
plt.xlabel('Sample Index')
plt.ylabel('Water Consumption (Liters)')
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.show()
plt.savefig('prediction_plot.png')  # saves it as a PNG image


# Plot Residual Errors
# residuals = y_test - y_pred
# plt.figure(figsize=(12, 6))
# plt.scatter(y_pred, residuals, color='red')
# plt.axhline(y=0, color='blue', linestyle='--')
# plt.title('Residual Errors (Actual - Predicted)')
# plt.xlabel('Predicted Consumption')
# plt.ylabel('Residual Error')
# plt.grid(True)
# plt.tight_layout()
# plt.show()



# After model.fit(...)
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")



