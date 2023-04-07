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
st.set_page_config(layout="wide", page_title='Ratio of land consumption rate to population growth rate', page_icon=":earth_asia:")
st.sidebar.markdown("SDG 11.3.1 Assessment")
# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("An assessment of Thailand's progress towards achieving SDG indicator 11.3.1 for the period 2000 - 2020")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This page presents the evaluation of indicators of sustainable development. Specifically, it focuses on Indicator 11.3.1, which is funded by the National Research Council of Thailand. ")
st.write("* The researchers responsible for Indicator 11.3.1 were Associate Professor Dr.Wenchao Xue.")
st.write("* For more information and detail contact: wenchao@ait.asia")

# =============================================================================
# Higlight of this study
# =============================================================================
st.subheader('Highlights')

st.write("- Urban expansion has outpaced population growth in most provinces and time intervals.")
st.write("- Inefficient land use was observed in most provinces during 2005-2010 and 2015-2020, with higher per capita land consumption than population growth. However, during 2010-2015, population growth exceeded urban expansion, resulting in a higher degree of urban compactness.")
st.write("- There is a need to regulate both urban expansion and population growth to ensure sustainable development.")
# =============================================================================
# Data Downloading
# =============================================================================

json1 = "Data/tha_admbnda_adm1_rtsd_201902_WGS.json"
with open(json1) as response:
    geo = json.load(response)
    
df = r"Data/LCRPGR_final_results.xlsx"
df = pd.read_excel(df)

df1 = df.copy()
df1.set_index('ADM1_EN', inplace=True)
df1 = df1.T

select = []
for c in df1.index:
    if c.startswith('Area_'):
        select.append(c)
select.sort()
Area = df1.loc[select]
select = []
for c in df1.index:
    if c.startswith('LCR_'):
        select.append(c)
LCR = df1.loc[select]
select = []
for c in df1.index:
    if c.startswith('Population_'):
        select.append(c)
select.sort()
Population = df1.loc[select]
select = []
for c in df1.index:
    if c.startswith('PGR_'):
        select.append(c)
select.sort()
PGR = df1.loc[select]
select = []
for c in df1.index:
    if c.startswith('LCRPGR_'):
        select.append(c)
select.sort()
LCRPGR = df1.loc[select]
Area.sort_index(inplace=True)
LCR.sort_index(inplace=True)
Population.sort_index(inplace=True)
PGR.sort_index(inplace=True)
LCRPGR.sort_index(inplace=True)

Population.index = ['2000','2005', '2010', '2015', '2020']
Population.index = pd.to_datetime(Population.index, format='%Y')
Population.index = Population.index.year

Area.index = ['2000','2005', '2010', '2015', '2020']
Area.index = pd.to_datetime(Area.index, format='%Y')
Area.index = Area.index.year

LCR.index = ['2000-2005', '2005-2010', '2010-2015', '2015-2020']
PGR.index = ['2000-2005', '2005-2010', '2010-2015', '2015-2020']
LCRPGR.index  = ['2000-2005', '2005-2010', '2010-2015', '2015-2020']


# =============================================================================
# Map graphice
# =============================================================================
st.header("Spatial distribution of SDG 11.3.1 in Thailand")
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
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# Bar Plot graphic
# =============================================================================
st.header("SDG 11.3.1 assessment and related value by selecting province in Thailand during 2000-2020")
# cloumns
col1, col2 = st.columns(2)
parameters = ['LCR', 'PGR', 'LCRPGR']
parameter = col1.multiselect('Choose the paramerts', parameters)

# Widgets: selectbox for province
sources = (df1.columns)
province = col2.multiselect("Choose province ", sources)

fig1 = go.Figure()
for para in parameter:
    
    for item in province:
        fig1.add_trace(
            go.Bar(
                x=globals()[para].index,
                y=globals()[para][item],
                hovertemplate="%{y:.2f}",
                
                name= f'{para}_{item}',
            ),
        )
fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#E3E3E3",
    plot_bgcolor="#FFFFFF",
    width=1200,
    height=900,
    title={'text' : f"SDG 11.3.1 assessment and related value by selecting province in Thailand"
           ,'x': 0.5, # Set the x anchor to the center of the chart
           'xanchor': 'center'},
    xaxis_title='Year',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1, use_container_width=True)
