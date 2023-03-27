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
st.title("Average share of the built-up area of cities that is open space for public use")

# =============================================================================
# Description
# =============================================================================
st.subheader('Description')
# Description of the website
st.write("* This page presents the evaluation of indicators of sustainable development. Specifically, it focuses on Indicator 11.7.1, which is funded by the National Research Council of Thailand. ")
st.write("* All of data was collected by Bangkok Metropolitan Administration (BMA)")
# Information about the researchers
st.write("* The researchers responsible for Indicator 11.7.1 were Associate Professor Dr. Ekebodin Winijkul and Mr. Pongsakorn Punpukdee.")
st.write("* For more information and detail contact: ekbordinw@ait.asia")

# =============================================================================
# Data downloading
# =============================================================================
df = pd.read_excel(r'Data/green_area.xlsx')
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['SDG 11.7.1'] = (df['Total park area'] + df['Area of roads'])*100 / df['Bangkok area']
df['BKK assessment'] = df['Total park area'] * 100 / df['Bangkok area']
df.set_index('Year', inplace=True)

# =============================================================================
# Data collection explaination
# =============================================================================
st.subheader('Data Visualization')
fig1 = go.Figure()
fig1.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Total park area'],
            # hovertemplate="%{y:.2f}",
            # showlegend=False,
            name='Total park area',
            mode='lines'
        ),
    )
fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#bcbcbc",
    plot_bgcolor="#f9e5e5",
    width=1200,
    height=600,
    title={'text' : f"The public green area in Bangkok (square meters)"
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
    yaxis_title='The public green area in Bangkok (square meters)',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1)


fig1 = go.Figure()
fig1.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Population Data'],
            # hovertemplate="%{y:.2f}",
            # showlegend=False,
            name='Population Data',
            mode='lines'
        ),
    )
fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#bcbcbc",
    plot_bgcolor="#f9e5e5",
    width=1200,
    height=600,
    title={'text' : f"The population number of people in Bangkok (people)."
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
    yaxis_title='The population number of people in Bangkok (people)',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1)
# =============================================================================
# Bar plot
# =============================================================================
fig1 = go.Figure()
assessment = ['SDG 11.7.1', 'BKK assessment']
for item in assessment:
    fig1.add_trace(
        go.Scatter(
            x=df.index,
            y=df[item],
            # hovertemplate="%{y:.2f}",
            # showlegend=False,
            name=item,
            mode='lines'
        ),
    )
fig1.update_layout(barmode="stack")
fig1.update_layout(
    paper_bgcolor="#bcbcbc",
    plot_bgcolor="#f9e5e5",
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
    xaxis_title='X-Axis Label',
    yaxis_title='Y-Axis Label',
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig1)