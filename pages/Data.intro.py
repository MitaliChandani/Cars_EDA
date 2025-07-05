import streamlit as st
import pandas as pd

st.title("📄 Data Introduction")

raw_df = pd.read_csv("Cars (1).csv")
clean_df = pd.read_csv("Cars_cleaned.csv")

st.header("🔍 Raw Dataset")
st.dataframe(raw_df)

st.markdown("---")

st.header("✅ Cleaned Dataset")
st.dataframe(clean_df)

st.markdown("---")

st.write("### Key Differences")
st.markdown("""
- *Missing Values* handled
- *Columns cleaned* (data types, units removed)
- *Consistent formatting* (e.g., bhp, kmpl as numeric)
- *Separated brand/model* in clean data
""")