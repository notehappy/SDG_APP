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
st.set_page_config(layout="wide", page_title='SDG 11.6.2', page_icon=":earth_asia:")
st.sidebar.markdown("SDG 11.6.2")
# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("An assessment of Thailand's progress towards achieving SDG indicator 11.6.2 for the period 2018 - 2021")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This website presents the evaluation of indicators of sustainable development. Specifically, it focuses on Indicator 11.6.2, which is funded by the National Research Council of Thailand. ")
st.write("* The indicator uses a PM2.5 concentration prediction model based on machine learning with the Extreme Gradient Boosting method.")
# Information about the population distribution
st.write("* The distribution of the population involved in the study was based on the Gridded Population of the World model.")

# Information about the researchers
st.write("* The researchers responsible for Indicator 11.6.2 were Associate Professor Dr. Ekebodin Winijkul and Mr. Pongsakorn Punpukdee.")

# =============================================================================
# Data Downloading
# =============================================================================

json1 = "Data/tha_admbnda_adm1_rtsd_201902_WGS.json"
with open(json1) as response:
    geo = json.load(response)

df = r"Data/sdg_monthly_TH(pro).csv"
df = pd.read_csv(df)

line_df = df.copy()
line_df.set_index('ADM1_EN', inplace=True)
line_df = line_df.T
line_df.index = pd.to_datetime(line_df.index, format='%B %Y')
line_df.index = line_df.index.strftime('%Y-%m')

average_TH = pd.DataFrame(line_df.mean(axis=1))
average_TH.rename(columns = {0:'SDG 11.6.2'}, inplace = True)


# =============================================================================
# Map graphice
# =============================================================================
st.header("Spatial distribution of SDG 11.6.2 by monthly average and provinces in Thailand")
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
            colorbar=dict(title="Unit of µg/m3")
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4.8,
        mapbox_center={"lat": 13.72917, "lon": 100.52389},
        width=800,
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
    ),
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)


# =============================================================================
# Bar Plot graphic
# =============================================================================
st.header("Average value of SDG 11.6.2. assessment by selecting province in Thailand during 2018-2021")
# Widgets: selectbox
sources = (line_df.columns)
province = st.multiselect("Choose province for SDG 11.6.2 assessment", sources)

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
fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#E3E3E3",
    plot_bgcolor="#FFFFFF",
    width=1200,
    height=600,
    title={'text' : f"An assessment of Thailand was conducting using the model developing of this study."
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
    yaxis_title='SDG 11.6.2 assessment',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1)

if st.checkbox("Show Dataframe"):
    st.table(data=df)



# =============================================================================
# Bar Plot graphic
# =============================================================================
# Setting up columns
st.header("Average value of SDG 11.6.2. assessment in Thailand during 2018-2021")
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
    title={'text' : f"An assessment of Thailand was conducting using the model developing of this study."
           ,'x': 0.5, # Set the x anchor to the center of the chart
           'xanchor': 'center'},
    xaxis_title='Year',
    yaxis_title='SDG 11.6.2 assessment',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig2)

