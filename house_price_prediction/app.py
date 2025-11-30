import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("data/house_data.csv")

# Preprocess data
X = pd.get_dummies(data[['Area','Bedrooms','Bathrooms','Location']], drop_first=True)
y = data['Price']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Streamlit UI
st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", 500, 5000)
bedrooms = st.number_input("Bedrooms", 1, 10)
bathrooms = st.number_input("Bathrooms", 1, 5)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])

# Prepare input
input_df = pd.DataFrame([[area, bedrooms, bathrooms, location]],
                        columns=['Area','Bedrooms','Bathrooms','Location'])
input_df = pd.get_dummies(input_df)
# Align with training data columns
for col in X.columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[X.columns]

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ₹{prediction:,.0f}")
