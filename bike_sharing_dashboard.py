import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

sns.set(style='dark')

st.subheader("Data") 
def workingday_df(df):
    explore1 = df.groupby(['season','workingday'])[['amount']].sum().reset_index()    
    explore1
    return explore1

def weather_df(df):
    weathersit_season = df.groupby(['season','weathersit'])[['amount']].sum().reset_index()    
    weathersit_season
    return weathersit_season

def sidebar(df):
    df["dateday"] = pd.to_datetime(df["dateday"])    
    min_date = df["dateday"].min()
    max_date = df["dateday"].max()    
    with st.sidebar:
        # Menambahkan logo perusahaan        
        st.image("https://c.pxhere.com/photos/d6/a5/bike_rental_apartments_for_rent_rent_deutsche_bahn_bicycles_cycling_locomotion-675616.jpg!d")
        def on_change():
            st.session_state.date = date
        date = st.date_input(label="Rentang Waktu",min_value=min_date,max_value=max_date,value=[min_date, max_date],on_change=on_change)
    return date

day_bike = pd.read_csv("bike_sharing_day.csv")

date = sidebar(day_bike)
if len(date) == 2:    
    main_df = day_bike[(day_bike["dateday"] >= str(date[0])) & (day_bike["dateday"] <= str(date[1]))]
else:    
    main_df = day_bike[(day_bike["dateday"] >= str(st.session_state.date[0])) & (day_bike["dateday"] <= str(st.session_state.date[1]))]

workingday_bike = workingday_df(main_df) 
weather_bike = weather_df(main_df)

# pengaruh hari kerja mempengeruhi pengunaan bike sharingst.header("Bike Sharing Dashboard :bike:")
st.subheader("Working Day")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=workingday_bike, x='season', y='amount', hue='workingday', ci=None)
ax.set_title("Perkembangan perbandingan jumlah sewa hari kerja dan hari libur tiap musim", loc="center", fontsize=30)
ax.set_ylabel("Jumlah Pengguna",fontsize=20)
ax.set_xlabel("Musim",fontsize=20)
ax.legend(title="day", fontsize=15)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
st.pyplot(fig)

# kondisi musim terhadap banyaknya pengguna bike sharing
st.subheader("Weather")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data = weather_bike, x='season', y='amount', hue='weathersit', ci=None)
ax.set_title("Pengaruh peminat pengguna sepeda berdasarkan cuaca", loc="center", fontsize=30)
ax.set_ylabel("Jumlah Pengguna",fontsize=20)
ax.set_xlabel("Musim",fontsize=20)
ax.legend(title="weathersit", fontsize=15)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
st.pyplot(fig)

copyright = "Copyright © " + "2023 | Bike Sharing Dashboard | All Rights Reserved | " + "Made by: @faiqshl"    
st.caption(copyright)