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
de = pd.read_csv(r'Data/emssion_lampang_modis.csv')
de.set_index('Date_Time', inplace=True)
json1 = r"Data/Grid_Lampang_WGS.geojson"
with open(json1) as response:
    geo = json.load(response)
compare = pd.read_csv(r'Data/comparing_VIIRS_MODIS_18_20.csv', index_col= 'Unnamed: 0')

# =============================================================================
# Map graphice for VIIRS
# =============================================================================
st.header('Air emissions from Active Fires Detected by VIIRS Sensor in Lampang based on Real-time')
st.warning('Caution: The spatial map may take some time to process and may result in a timelapse.')
left_column, right_column = st.columns([1, 1])
choice = df.index.unique()
choice = choice.sort_values(ascending=False)
choice_selected = left_column.selectbox("Select time for show distribution", choice)
choice1 = df.columns[1:]
choice_selected1 = right_column.selectbox("Select air pollutant types", choice1)
df1 = df.loc[choice_selected]

df2 = df1
df2.drop('Id', axis = 1, inplace = True)
df2 = pd.DataFrame(df2.sum(), columns=['emisson (Kg)'])
# Geographic Map
st.write(f'{style_title_graph}<p class="center-text bold-color-text">"{choice_selected1} Emissions from Active Fires Detected by VIIRS Sensor in Lampand on {choice_selected}"</p>', unsafe_allow_html=True)
left_column1, right_column1 = st.columns([1, 1])
with left_column1:
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson= geo,
            locations=df['Id'],
            featureidkey="properties.Id",
            z=df1[choice_selected1],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
            name = f'{choice_selected1} Emissions from Active Fires Detected by MODIS Sensor in Lampand on {choice_selected}',
            colorbar=dict(title="Unit of Kg")
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=7,
        mapbox_center={"lat": 18.34, "lon": 99.5},
        # width=800,
        # height=600,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)

with right_column1:
    fig2 = go.Figure()
    for i in range(df2.shape[0]):
        fig2.add_trace(
            go.Bar(
                x=[df2.index[i]],
                y=[df2.iloc[i,0]],
                hovertemplate="%{y:.2f}",
                name= f'{df2.index[i]}',
        ),
        )
    # fig2.update_layout(barmode="stack")
    fig2.update_layout(
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
    xaxis_title='Types of emission detected by VIIRS ',
    yaxis_title='Amount of emission in Kg',
    )
    st.plotly_chart(fig2)

# =============================================================================
# Map graphice for MODIS
# =============================================================================
st.header('Air emissions from Active Fires Detected by MODIS Sensor in Lampang based on Real-time')
st.warning('Caution: The spatial map may take some time to process and may result in a timelapse.')
left_column2, right_column2 = st.columns([1, 1])
choice3 = de.index.unique()
choice3 = choice3.sort_values(ascending=False)
choice_selected3 = left_column2.selectbox("Select time for show distribution", choice3)
choice4 = de.columns[1:]
choice_selected4 = right_column2.selectbox("Select air pollutant types", choice4, key='option1')
de1 = de.loc[choice_selected3]

de2 = de1
de2.drop('Id', axis = 1, inplace = True)
de2 = pd.DataFrame(de2.sum(), columns=['emisson (Kg)'])
# Geographic Map
st.write(f'{style_title_graph}<p class="center-text bold-color-text">"{choice_selected4} Emissions from Active Fires Detected by MODIS Sensor in Lampang on {choice_selected3}"</p>', unsafe_allow_html=True)
left_column1, right_column1 = st.columns([1, 1])
with left_column1:
    fig3 = go.Figure(
        go.Choroplethmapbox(
            geojson= geo,
            locations=de['Id'],
            featureidkey="properties.Id",
            z=de1[choice_selected1],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
            name = f'{choice_selected4} Emissions from Active Fires Detected by MODIS Sensor in Lampand on {choice_selected3}',
            colorbar=dict(title="Unit of Kg")
        )
    )
    fig3.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=7,
        mapbox_center={"lat": 18.34, "lon": 99.5},
        # width=800,
        # height=600,
    )
    fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig3)

with right_column1:
    fig4 = go.Figure()
    for i in range(de2.shape[0]):
        fig4.add_trace(
            go.Bar(
                x=[de2.index[i]],
                y=[de2.iloc[i,0]],
                hovertemplate="%{y:.2f}",
                name= f'{de2.index[i]}',
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
    )
    st.plotly_chart(fig4)

# =============================================================================
# Bar plot comparing MODIS and VIIRS
# =============================================================================
st.header("Comparison of Burn Area Estimates between MODIS and VIIRS Sensors for 2018-2020")
fig5 = go.Figure()

fig5.add_trace(
    go.Bar(
        x=compare.index,
        y=compare['VIIRS_AREA (km2)'],
        hovertemplate="%{y:.2f}",
        name= f'{de2.index[i]}',
),
)
fig5.add_trace(
    go.Bar(
        x=compare.index,
        y=compare['MODIS_AREA (km2)'],
        hovertemplate="%{y:.2f}",
        name= f'{de2.index[i]}',
),
)
# fig2.update_layout(barmode="stack")
fig5.update_layout(
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
)
st.plotly_chart(fig5, use_container_width=True)