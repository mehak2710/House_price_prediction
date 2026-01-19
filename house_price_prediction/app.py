import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Title
st.title("🏡 Simple House Price Prediction")

# Load dataset
data = pd.read_csv("data/house_prices.csv")
st.subheader("Dataset Preview")
st.write(data.head())

# Features and target
X = data[['Bedrooms', 'Bathrooms', 'Size_sqft', 'Age']]
y = data['Price']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

# User input via sliders
st.sidebar.header("Enter House Details")
bedrooms = st.sidebar.slider("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.sidebar.slider("Bathrooms", min_value=1, max_value=5, value=2)
size = st.sidebar.slider("Size (sqft)", min_value=100, max_value=10000, value=1500)
age = st.sidebar.slider("Age of House (years)", min_value=0, max_value=100, value=10)

# Prepare input
input_data = [[bedrooms, bathrooms, size, age]]
input_scaled = scaler.transform(input_data)

# Predict
prediction = model.predict(input_scaled)

# Display predicted price
st.subheader("💰 Estimated House Price")
st.success(f"${prediction[0]:,.2f}")

# Compare with dataset average
avg_price = data['Price'].mean()
st.subheader("📊 Comparison with Dataset Average")
if prediction[0] < avg_price:
    st.info(f"Your house price is below average (${avg_price:,.2f}) in the dataset ✅")
elif prediction[0] > avg_price:
    st.warning(f"Your house price is above average (${avg_price:,.2f}) ⚠️")
else:
    st.write("Your house price is around the dataset average.")
