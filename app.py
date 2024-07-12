import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
st.header('SDT Project')

df['model_year'] = df['model_year'].fillna(df['model_year'].median())

fig = px.scatter(df, x='model_year',
                 y='price',
                 title='Price and Model Year',
                 labels={'model_year':'Model Year', 'price':'Sell Price'})
fig.update_yaxes(range=[5000, 200000])
st.plotly_chart(fig)

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type':'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)
