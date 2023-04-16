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
# Template
# =============================================================================
css_file = r'styles/main.css'
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)
st.title("Emission Real-time from active fire using VIIRS, MODIS and Himawari sensor in Lampang")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This website presents Real-time emission using the active fire detected by VIIRS, MODIS and Himawari(developing) based on Real-time")
# Information about the researchers
st.write("* The researchers were Associate Professor Dr. Ekebodin Winijkul and Mr. Pongsakorn Punpukdee.")
st.write("* For more information and detail contact: ekbordinw@ait.asia")


# =============================================================================
# Text style
# =============================================================================
# Set the CSS styles for bold text and a custom color
style_title_graph = '''
    <style>
        .center-text {
            text-align: center;
        }
        .bold-color-text {
            font-weight: bold;
            color: #ff5733;
        }
    </style>
'''
# =============================================================================
# Data Downloading
# =============================================================================
df = pd.read_csv(r'Data/emssion_lampang_viirs.csv')
df.set_index('Date_Time', inplace=True)
da = pd.read_csv(r'Data/emssion_lampang_modis.csv')
da.set_index('Date_Time', inplace=True)
db = pd.read_csv(r'Data/emssion_lampang_himawari.csv')
db.set_index('Date_Time', inplace=True)
json1 = r"Data/Grid_Lampang_WGS.geojson"
with open(json1) as response:
    geo = json.load(response)
compare = pd.read_csv(r'Data/comparing_VIIRS_MODIS_HIMAWARI_20_22.csv', index_col= 'LU_CODE')

# =============================================================================
# Map graphice for HIMAWARI
# =============================================================================
st.header('Air emissions from Active Fires Detected by MODIS Sensor in Lampang based on Real-time')
st.warning('Caution: The spatial map may take some time to process and may result in a timelapse.')
left_column3, right_column3 = st.columns([1, 1])
choice5 = db.index.unique()
choice5 = choice5.sort_values(ascending=False)
choice_selected5 = left_column3.selectbox("Select time for show distribution", choice5)
choice6 = db.columns[1:]
choice_selected6 = right_column3.selectbox("Select air pollutant types", choice6, key='option1')
db1 = db.loc[choice_selected5]

db2 = db1
db2.drop('Id', axis = 1, inplace = True)
db2 = pd.DataFrame(db2.sum(), columns=['emisson (Kg)'])
# Geographic Map
st.write(f'{style_title_graph}<p class="center-text bold-color-text">"{choice_selected6} Emissions from Active Fires Detected by MODIS Sensor in Lampang on {choice_selected5}"</p>', unsafe_allow_html=True)
left_column5, right_column5 = st.columns([1, 1])
with left_column5:
    fig3 = go.Figure(
        go.Choroplethmapbox(
            geojson= geo,
            locations=db['Id'],
            featureidkey="properties.Id",
            z=db1[choice_selected6],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
            name = f'{choice_selected6} Emissions from Active Fires Detected by MODIS Sensor in Lampand on {choice_selected5}',
            colorbar=dict(title="Unit of Kg")
        )
    )
    fig3.update_layout(
        paper_bgcolor="#E3E3E3",
        mapbox_style="carto-positron",
        mapbox_zoom=7,
        mapbox_center={"lat": 18.34, "lon": 99.5},
        # width=800,
        # height=600,
        font=dict(color='black')
    )
    fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig3, use_container_width=True)

with right_column5:
    fig4 = go.Figure()
    for i in range(db2.shape[0]):
        fig4.add_trace(
            go.Bar(
                x=[db2.index[i]],
                y=[db2.iloc[i,0]],
                hovertemplate="%{y:.2f}",
                name= f'{db2.index[i]}',
        ),
        )
    # fig2.update_layout(barmode="stack")
    fig4.update_layout(
        paper_bgcolor="#E3E3E3",
        plot_bgcolor="#FFFFFF",
        # width=900,
        # height=1000,
        # title={'text' : f"SDG 11.2.1 assessment and related value by selecting province in Thailand"
        #     ,'x': 0.5, # Set the x anchor to the center of the chart
        #     'xanchor': 'center'},
        margin=dict(l=50, r=50, t=50, b=50),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis_title='Types of emission detected by MODIS ',
        yaxis_title='Amount of emission in Kg',
        font=dict(
            color='black',
        ),
        xaxis=dict(
            title_font=dict(
                color='black',
            ),
            tickfont=dict(
                color='black',
            )
        ),
        yaxis=dict(
            title_font=dict(
                color='black',
            ),
            tickfont=dict(
                color='black',
            )
        )
    )
    st.plotly_chart(fig4, use_container_width=True)