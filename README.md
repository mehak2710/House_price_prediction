
# 🏡 Simple House Price Prediction App

A **beginner-friendly Streamlit app** that predicts house prices based on simple features like bedrooms, bathrooms, size, and age. Includes real-time predictions and a comparison with the dataset average for better user insights.

---

## **Features**

* Real-time prediction using **sliders**.
* Comparison of predicted price with **dataset average**.
* Clean, interactive **Streamlit interface**.
* Dataset preview directly in the app.
* Easy deployment on **Streamlit Community Cloud**.

---

## **Dataset**

* CSV file: `data/house_prices.csv`
* Contains columns:

  * `Bedrooms` → Number of bedrooms
  * `Bathrooms` → Number of bathrooms
  * `Size_sqft` → Size of the house in square feet
  * `Age` → Age of the house in years
  * `Price` → House price in USD

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
streamlit run app.py
```

---

## **Future Enhancements**

* Interactive **price visualization charts**.
* Multiple predictions via **CSV upload**.
* Suggested improvements based on house features.
