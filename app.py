import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
st.header('SDT Project')

fig = px.scatter(df, x='model_year', y='price', title='Price and Model Year', labels={'model_year':'Model Year', 'price':'Sell Price'})
st.plotly_chart(fig)

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type':'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)