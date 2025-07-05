import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cars EDA Project", page_icon="🚗", layout="centered")

st.title("🚗 Cars Exploratory Data Analysis (EDA) Project")
st.subheader("Understand the Used Car Market with Data-Driven Insights")

car_image = Image.open("cars.jpg") 
st.image(car_image, caption="Used Cars Market", use_column_width=True)


st.markdown("""
### Problem Statement

The used car market is expanding rapidly, but buyers often struggle to make informed decisions due to lack of clear and comprehensive data insights.

This project provides an in-depth Exploratory Data Analysis (EDA) on used car listings data to reveal important trends and patterns about car features, pricing, and market dynamics.

By exploring factors such as *location, manufacturing year, mileage, fuel type, and price*, this app empowers buyers and sellers to understand market behavior, set fair prices, and make confident, data-driven decisions.
""")


st.markdown("---")
st.markdown("Use the sidebar to navigate through the data introduction, detailed analysis, and visualizations.")
