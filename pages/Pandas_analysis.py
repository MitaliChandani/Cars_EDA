import streamlit as st
import pandas as pd

st.title("📊 Pandas Analysis")

df = pd.read_csv("Cars_cleaned.csv")

st.subheader("1. Basic Info")
st.write(df.info())

st.subheader("2. Summary Statistics")
st.write(df.describe())

st.subheader("3. Null Values")
st.write(df.isnull().sum())

st.subheader("4. Unique Value Counts")
for col in ['Fuel_Type', 'Transmission', 'Owner_Type', 'Colour', 'Brand']:
    st.write(f"{col}: {df[col].nunique()} unique values")
    st.write(df[col].value_counts())

st.subheader("5. Top 5 Most Driven Cars")
st.write(df.sort_values(by='Kilometers_Driven', ascending=False)[['Name', 'Kilometers_Driven']].head())

st.subheader("6. Average Price by Brand")
st.write(df.groupby("Brand")["Price"].mean().sort_values(ascending=False))