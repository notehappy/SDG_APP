# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:10:54 2023

@author: Labtop
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots
from PIL import Image
import os
st.set_page_config(layout="wide", page_title='PM2.5 model of this study', page_icon=":earth_asia:")
st.sidebar.markdown("PM25 Predicting Model")
# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("PM2.5 concentration in Thailand using PM2.5 model of study")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This website presents the evaluation of indicators of sustainable development. Specifically, it focuses on Indicator 11.6.2, which is funded by the National Research Council of Thailand. ")
st.write("* The PM2.5 concentration prediction model uses the Extreme Gradient Boosting method with AOD images, WRF-model(TMD) and PM2.5 concentration (PCD).")
# Information about the researchers
st.write("* The researchers responsible for Indicator 11.6.2 were Associate Professor Dr. Ekebodin Winijkul and Mr. Pongsakorn Punpukdee.")
st.write("* For more information and detail contact: ekbordinw@ait.asia")


# =============================================================================
# Data Downloading
# =============================================================================

json1 = "Data/tha_admbnda_adm1_rtsd_201902_WGS.json"
with open(json1) as response:
    geo = json.load(response)
    
df = r"Data/PM25_monthly_TH(pro).csv"
df = pd.read_csv(df)

line_df = df.copy()
line_df.set_index('ADM1_EN', inplace=True)
line_df = line_df.T
line_df.index = pd.to_datetime(line_df.index, format='%B %Y')
line_df.index = line_df.index.strftime('%Y-%m')

average_TH = pd.DataFrame(line_df.mean(axis=1))
average_TH.rename(columns = {0:'SDG 11.6.2'}, inplace = True)

accuracy = pd.read_csv(r'Data/accuracy_model.csv')
accuracy.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
accuracy.drop(columns='month', inplace=True)
accuracy.set_index('Date', inplace=True)
# =============================================================================
# Map graphice
# =============================================================================
st.header('Our study model was used to determine the monthly average PM2.5 concentration in various provinces throughout Thailand.')
st.warning('Caution: The spatial map may take some time to process and may result in a timelapse.')
if st.checkbox("Show Map"):
    left_column, right_column = st.columns([1, 1])
    choice = df.columns[1:]
    choice_selected = left_column.selectbox("Select monthly and year average", choice)
    # Geographic Map
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson= geo,
            locations=df['ADM1_EN'],
            featureidkey="properties.ADM1_EN",
            z=df[choice_selected],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
            name = 'PM 2.5 concentration (µg/m3)'            ,
            colorbar=dict(title="Unit of µg/m3")
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4.8,
        mapbox_center={"lat": 13.72917, "lon": 100.52389},
        width=800,
        height=600,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# Bar Plot graphic
# =============================================================================
st.header("Average value of PM2.5 concentration by selecting province in Thailand during 2018-2021")
# Widgets: selectbox
sources = (line_df.columns)
province = st.multiselect("Choose province for PM2.5 concentration", sources)

fig1 = go.Figure()

for item in province:
    fig1.add_trace(
        go.Bar(
            x=line_df.index,
            y=line_df[item],
            hovertemplate="%{y:.2f}",
            # showlegend=False,
            name=item,
        ),
    )
# fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#E3E3E3",
    plot_bgcolor="#FFFFFF",
    width=1200,
    height=600,
    title={'text' : f"Average value of PM2.5 concentration using the model developing of this study."
           ,'x': 0.5, # Set the x anchor to the center of the chart
           'xanchor': 'center'},
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis_title='Year',
    yaxis_title='PM2.5 concentration (micrograms per cubic meter)',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1, use_container_width=True)

if st.checkbox("Show Dataframe"):
    st.table(data=df)

# =============================================================================
# Bar Plot graphic
# =============================================================================
# Setting up columns
st.header("Average value of PM2.5 concentration in Thailand during 2018-2021")
fig2 = go.Figure(
     go.Bar(
         x=average_TH.index,
         y=average_TH['SDG 11.6.2'],
         hovertemplate="%{y:.2f}",
         # showlegend=False,
     ),
 )
fig2.update_layout(
    paper_bgcolor="#E3E3E3",
    plot_bgcolor="#FFFFFF",
    width=1200,
    height=600,
    title={'text' : f"An assessment of Thailand was conducting using the model developing of this study"
           ,'x': 0.5, # Set the x anchor to the center of the chart
           'xanchor': 'center'},
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0,
        xanchor="right",
        x=1
    ),
    xaxis_title='Year',
    yaxis_title='PM2.5 concentration (micrograms per cubic meter)',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig2, use_container_width=True)


# =============================================================================
# Bar Plot graphic
# =============================================================================
# Setting up columns
st.header("Accuracy of Predicted PM2.5 concentration model comparing with PCD monitoring data")
fig3 = go.Figure()
fig3.add_trace(
    go.Scatter(
        x=accuracy.index,
        y=accuracy['Predicted_PM2.5'],
        hovertemplate="%{y:.2f}",
        name='Predicted_PM2.5',
        mode = 'lines'
    )  
)
fig3.add_trace(
    go.Scatter( x=accuracy.index,
        y=accuracy['PM2.5_station'],
        hovertemplate="%{y:.2f}",
        # showlegend=False,
        name='PM2.5_station',
        mode = 'lines'
         ),
    
)

fig3.update_layout(barmode="stack")
fig3.update_layout(
    paper_bgcolor="#E3E3E3",
    plot_bgcolor="#FFFFFF",
    width=1200,
    height=600,
    title={'text' : f"Accuracy model of Predicted PM2.5 concentration."
           ,'x': 0.5, # Set the x anchor to the center of the chart
           'xanchor': 'center'},
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis_title='Year',
    yaxis_title='PM2.5 concentration (micrograms per cubic meter)',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig3, use_container_width=True)
st.caption('Accuracy of model (RMSE = 15.56 µg/m3 and R2 = 0.54)')