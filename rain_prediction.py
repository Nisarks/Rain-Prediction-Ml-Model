import joblib
import pandas as pd

# Load trained model and scaler

model = joblib.load("rain_model.pkl")
scaler = joblib.load("scaler.pkl")


# Get user input

try:
    humidity = float(input("Enter Humidity (0-100): "))
    pressure = float(input("Enter Pressure (hPa): "))
    cloud_cover = float(input("Enter Cloud Cover (0-100): "))
except ValueError:
    print(" Please enter valid numeric values.")
    exit()

# Validate input

if not (0 <= humidity <= 100):
    print(" Humidity must be between 0 and 100.")
    exit()

if pressure <= 0:
    print(" Pressure must be greater than 0.")
    exit()

if not (0 <= cloud_cover <= 100):
    print(" Cloud Cover must be between 0 and 100.")
    exit()

# ============================
# Create DataFrame
# (same feature names used during training)

new_data = pd.DataFrame({
    "Humidity": [humidity],
    "Pressure": [pressure],
    "Cloud_Cover": [cloud_cover]
})

new_data_scaled = scaler.transform(new_data)

prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)

print("\n========== Prediction Result ==========")

if prediction[0] == 1:
    print("🌧 Prediction : Rain")
    print(f"Confidence : {probability[0][1]*100:.2f}%")
else:
    print("☀ Prediction : No Rain")
    print(f"Confidence : {probability[0][0]*100:.2f}%")
