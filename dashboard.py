import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/day.csv')
data = pd.read_csv('data/hour.csv')

# Sidebar
st.sidebar.title("Bike Sharing Analysis")
season = st.sidebar.selectbox('Select Season', data['season'].unique())

# Filter data
filtered_data = data[data['season'] == season]

# Main
st.title('Bike Sharing Dashboard')
st.write('Rata-rata Penggunaan Sepeda Berdasarkan Musim')

# Plot
season_data = data.groupby('season')['count'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='season', y='count', data=season_data, ax=ax)
st.pyplot(fig)

# Correlation Heatmap
st.write('Korelasi antar Fitur')
correlation = data.corr()
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
