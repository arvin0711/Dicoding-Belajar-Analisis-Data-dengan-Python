import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# import dataset
day_df = pd.read_csv('https://raw.githubusercontent.com/arvin0711/Dicoding-Belajar-Analisis-Data-dengan-Python/main/day_clean.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/arvin0711/Dicoding-Belajar-Analisis-Data-dengan-Python/main/hour.csv')

# Judul dashboard
st.title('Bike Rental Analysis Dashboard')

# Sidebar
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    min_date = pd.to_datetime(day_df["dteday"].min()).date()
    max_date = pd.to_datetime(day_df["dteday"].max()).date()
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date)
    )
# Membuat visualisasi jumlah penyewaan sepede berdasarkan hari kerja
st.subheader('Bike Rentals by Working Day')
plt.figure(figsize=(8, 6))
byworkingday_df = day_df.groupby(by="workingday")["instant"].nunique().reset_index()
byworkingday_df.rename(columns={
    "instant": "sum"
}, inplace=True)
sns.barplot(x=byworkingday_df["workingday"], y=byworkingday_df["sum"])
plt.title('Bike Number When Working Day')
plt.xlabel('Working Day')
plt.ylabel(None)
plt.xticks([0, 1], ['Non-Working Day', 'Working Day'])
st.pyplot()



# Menghitung rata-rata penyewaan sepeda berdasarkan kondisi cuaca
avg_rentals_by_weather = hour_df.groupby('weathersit')['cnt'].mean()

# membuat visualisasi rata-rata penyewaan sepeda berdasarkan kondisi cuaca
st.subheader('Average Bike Rentals by Weather Situation')
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_rentals_by_weather.index, y=avg_rentals_by_weather.values)
plt.title('Average Bike Rentals by Weather Situation')
plt.xlabel('Weather Situation')
plt.ylabel('Average Rentals')
plt.xticks([0, 1, 2, 3], ['Clear', 'Cloudy', 'Light Rain', 'Heavy Rain'])
st.pyplot()

# Disable the warning for global use of pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)
