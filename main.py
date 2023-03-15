import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('happy.csv')

st.title("In search for happiness")

metric_list = {"Happiness": data.happiness, "GDP": data.gdp,
               "Social support": data.social_support,
               "Life expectancy": data.life_expectancy,
               "Freedom to make life choices": data.freedom_to_make_life_choices,
               "Generosity": data.generosity, "Corruption": data.corruption}

x_ax_select = st.selectbox("Select the data for the x-axis",
                           options=metric_list)
y_ax_select = st.selectbox("Select the data for the y-axis",
                           options=metric_list)

st.subheader(f"{x_ax_select} vs. {y_ax_select}")

figure = px.scatter(x=metric_list[x_ax_select], y=metric_list[y_ax_select], labels={'x': x_ax_select, 'y': y_ax_select})

st.plotly_chart(figure)