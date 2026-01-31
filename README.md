# Turkey CO₂ Emission Forecasting (SKA 13)

## Proje Hakkında
Bu çalışma, Birleşmiş Milletler Sürdürülebilir Kalkınma Amaçları kapsamında yer alan  
**SKA 13: İklim Eylemi** doğrultusunda gerçekleştirilmiştir.  
Türkiye’nin geçmiş CO₂ emisyon verileri analiz edilerek, geleceğe yönelik emisyon
tahminleri yapılmıştır.

---

## Amaç
- Türkiye’nin **2010–2023** CO₂ emisyon verilerini incelemek  
- Geçmiş eğilimleri analiz etmek  
- **Doğrusal Regresyon** modeli ile 2024 sonrası için **30 yıla kadar** emisyon tahmini yapmak  

---

## Veri Seti
- **Ülke:** Türkiye  
- **Gösterge:** CO₂ Emisyonu (Mt CO₂e)  
- **Zaman Aralığı:** 2010 – 2023  
- **Kaynak:** World Bank Open Data, TÜİK  

Veriler Excel formatında alınmış, Python ile analiz edilmiştir. Eksik veya aykırı
değer bulunmamaktadır.

---

## Yöntem
- **Model:** Doğrusal Regresyon (Linear Regression)  
- **Bağımsız Değişken:** Yıl  
- **Bağımlı Değişken:** CO₂ Emisyonu  
- **Kütüphaneler:** Python, Scikit-learn  

### Performans Metrikleri
- **R²:** 0.872  
- **RMSE:** 16.570  

---

##  Bulgular
- **2010–2023:** CO₂ emisyonlarında genel artış eğilimi  
- **2024–2053:** Mevcut eğilimin devam etmesi durumunda artışın sürmesi beklenmektedir  

---

##  Uygulama
Proje, **Streamlit tabanlı interaktif bir web uygulaması** olarak geliştirilmiştir.
Kullanıcılar:
- Tahmin süresini seçebilir
- Geçmiş ve geleceğe yönelik CO₂ emisyonlarını grafikler üzerinden inceleyebilir

### Çalıştırma
```bash
pip install -r requirements.txt
streamlit run Co2_forecasting_app_linear.py

