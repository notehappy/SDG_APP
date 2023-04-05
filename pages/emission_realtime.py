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
st.set_page_config(layout="wide", page_title='Emission Real-time from active fire in Lampang Province', page_icon=":earth_asia:")
st.sidebar.markdown("Emission Real-time")
# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("Emission Real-time from active fire using VIIRS sensor in Lampang")


# =============================================================================
# Data Downloading
# =============================================================================

df = pd.read_csv(r'Data/emssion_lampang.csv')
json1 = r"Data/Grid_Lampang_WGS.geojson"
with open(json1) as response:
    geo = json.load(response)

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
            locations=df['Id'],
            featureidkey="properties.Id",
            z=df['PM10'],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
            name = 'PM 2.5 concentration (µg/m3)'
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
    st.plotly_chart(fig)
