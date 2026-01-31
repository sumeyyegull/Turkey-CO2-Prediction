import streamlit as st
st.set_page_config(layout="centered")

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# -------------------------------
# 1) Sayfa Başlığı 
# -------------------------------
st.title("Türkiye CO₂ Emisyon Tahmin Uygulaması")

# -------------------------------
# 2) Veriyi Yükle
# -------------------------------
df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Year_int'] = df['Year'].dt.year

# -------------------------------
# 3) Model
# -------------------------------
X = df[['Year_int']]
y = df['CO2']

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# 4) Model Performansı
# -------------------------------
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

st.subheader("Model Performansı")
st.write(f"R² Skoru: {r2:.3f}")
st.write(f"RMSE: {rmse:.3f}")

# -------------------------------
# 5) Görsel 
# -------------------------------
try:
    image = Image.open("co2_hamveri.jpg")
    st.image(image)
except:
    st.info("Görsel bulunamadı, devam ediliyor.")

# -------------------------------
# 6) Slider
# -------------------------------
year = st.slider("Kaç yıl ileri tahmin yapmak istiyorsunuz?", 1, 30, step=1)

# -------------------------------
# 7) Tahmin
# -------------------------------
if st.button("Predict"):
    last_year = df['Year_int'].max()

    future_years = pd.DataFrame({
        "Year_int": range(last_year + 1, last_year + 1 + year)
    })

    future_pred = model.predict(future_years)

    pred_df = pd.DataFrame({
        "Year": future_years['Year_int'],
        "CO2": future_pred
    }).set_index("Year")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("Tahmin Tablosu")
        st.dataframe(pred_df)

    with col2:
        st.subheader("CO₂ Emisyon Grafiği")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df['Year_int'], df['CO2'], linestyle='--', label='Geçmiş Veriler')
        ax.plot(pred_df.index, pred_df['CO2'], label='Tahmin')
        ax.set_xlabel("Yıl")
        ax.set_ylabel("CO₂ Emisyonu")
        ax.legend()
        st.pyplot(fig)