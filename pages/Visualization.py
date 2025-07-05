import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualization and Analysis")

df = pd.read_csv("Cars_cleaned.csv")

analysis_type = st.radio("Choose Analysis Type", ("Univariate", "Bivariate", "Multivariate"))

if analysis_type == "Univariate":
    st.header("Univariate Analysis")
    column = st.selectbox("Select column for univariate analysis", df.columns)

    if pd.api.types.is_numeric_dtype(df[column]):
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        ax.set_title(f'Distribution of {column}')
        st.pyplot(fig)
        
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[column], ax=ax2)
        ax2.set_title(f'Boxplot of {column}')
        st.pyplot(fig2)
    else:
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f'Count plot of {column}')
        st.pyplot(fig)

elif analysis_type == "Bivariate":
    st.header("Bivariate Analysis")
    col1 = st.selectbox("Select first column (usually numeric)", df.select_dtypes(include='number').columns)
    col2 = st.selectbox("Select second column", df.columns)

    if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
        ax.set_title(f'Scatter plot between {col1} and {col2}')
        st.pyplot(fig)
    elif pd.api.types.is_numeric_dtype(df[col1]) and not pd.api.types.is_numeric_dtype(df[col2]):
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col2], y=df[col1], ax=ax)
        ax.set_title(f'Boxplot of {col1} grouped by {col2}')
        st.pyplot(fig)
    else:
        st.write("Bivariate plot not available for selected combination.")

elif analysis_type == "Multivariate":
    st.header("Multivariate Analysis")

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    st.subheader("Correlation Heatmap")
    selected_heatmap_cols = st.multiselect("Select numeric columns for heatmap", numeric_cols, default=numeric_cols[:5])
    if len(selected_heatmap_cols) >= 2:
        fig, ax = plt.subplots()
        sns.heatmap(df[selected_heatmap_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)
    else:
        st.write("Select at least two numeric columns for heatmap.")

    st.subheader("Scatter / Bar plot with Hue")
    all_cols = df.columns.tolist()
    x_col = st.selectbox("Select X-axis column", all_cols, key='xcol')
    y_col = st.selectbox("Select Y-axis column", all_cols, key='ycol')
    hue_col = st.selectbox("Select Hue (legend) column", [None] + all_cols, key='huecol')

    plot_type = st.radio("Select plot type", ("Scatter Plot", "Bar Plot"))

    if x_col and y_col:
        fig, ax = plt.subplots()
        try:
            if plot_type == "Scatter Plot":
                sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col if hue_col != 'None' else None, ax=ax)
            else:  
                sns.barplot(data=df, x=x_col, y=y_col, hue=hue_col if hue_col != 'None' else None, ax=ax)
            ax.set_title(f'{plot_type} of {y_col} vs {x_col} grouped by {hue_col}')
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting: {e}")