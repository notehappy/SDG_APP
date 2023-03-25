# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:22:41 2023

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
st.set_page_config(layout="wide", page_title='Proportion of population that has convenient access to public transport, by sex, age and persons with disabilities', page_icon=":earth_asia:")
st.sidebar.markdown("SDG 11.2.1 Assessment")

# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("An assessment of Thailand's progress towards achieving SDG indicator 11.2.1 for 2020")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This page presents the evaluation of indicators of sustainable development. Specifically, it focuses on Indicator 11.2.1, which is funded by the National Research Council of Thailand. ")
# Information about the population distribution
st.write("* The distribution of the population involved in the study was based on the Gridded Population of the World model.")
# Information about the researchers
st.write("* The researchers responsible for Indicator 11.2.1 were Associate Professor Dr. Ekebodin Winijkul and Mr.Pongsakorn Punpukdee.")


# =============================================================================
# Data Downloading
# =============================================================================
json1 = "Data/six_provinces_WGS.json"
with open(json1) as response:
    geo = json.load(response)

percent_normanl = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='percent_normal')
percent_normanl.set_index('Province', inplace = True)

number_normal = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='number_normal')
number_normal.set_index('Province', inplace=True)

percent_dis = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='percent_dis')
percent_dis.set_index('Province', inplace=True)

number_dis = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='number_dis')
number_dis.set_index('Province', inplace=True)
# =============================================================================
# Map graphice
# =============================================================================
st.header("Spatial distribution of SDG 11.2.1 in Thailand")

left_column, right_column = st.columns([1, 1])
choice = ['normal_person', 'disabled person']
choice_selected = left_column.selectbox("Select the type of person", choice)

choice1 = ['number of people', 'percentage of people']
choice_selected1 = right_column.selectbox("Select the type of person", choice1)

st.warning('Caution: The spatial map may take some time to process and may result in a timelapse.')




if st.checkbox("Show Map"):
    left_column, right_column = st.columns([1, 1])
    choice = df.columns[1:]
    choice_selected = left_column.selectbox("Select the parameter", choice)
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