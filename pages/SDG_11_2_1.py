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

percent_normal = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='percent_normal')
percent_normal.set_index('Province', inplace = True)

number_normal = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='number_normal')
number_normal.set_index('Province', inplace=True)

percent_dis = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='percent_dis')
percent_dis.set_index('Province', inplace=True)

number_dis = pd.read_excel(r'Data/Public_transport.xlsx', sheet_name='number_dis')
number_dis.set_index('Province', inplace=True)
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
# Map graphice
# =============================================================================
st.header("Spatial distribution of SDG 11.2.1 in Thailand")

left_column, right_column = st.columns([1, 1])
choice1 = ['normal person', 'disabled person']
choice_selected1 = left_column.selectbox("Select the type of person", choice1)

choice2 = ['number of people', 'percentage of people']
choice_selected2 = right_column.selectbox("Select the type of person", choice2)

if choice_selected1 == 'normal person' and choice_selected2 == 'number of people':
    left_column1, right_column1 = st.columns([1, 1])
    choice3 = ['All public transportation', 'Bus', 'Ferry', 'Railway','Train']
    choice_selected3 = left_column1.selectbox("Select the type of public transportration", choice3)
    choice4 = ['Children', 'Adults', 'Older Adults', 'Nonidentified']
    choice_selected4 = right_column1.selectbox("Select the age ranges", choice4)
    df = number_normal[number_normal['Age group'] == f'{choice_selected4}']
    st.write(f'{style_title_graph}<p class="center-text bold-color-text">The number of people can access to public transportration in BMR during 2020</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        fig = go.Figure(
            go.Choroplethmapbox(
                geojson= geo,
                locations=df.index,
                featureidkey="properties.ADM1_EN",
                z=df[f'{choice_selected3}'],
                colorscale="sunsetdark",
                # zmin=0,
                # zmax=500000,
                marker_opacity=0.5,
                marker_line_width=0,
            )
        )
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=8.2,
            mapbox_center={"lat": 13.72917, "lon": 100.52389},
            # width = 900,
            # height = 1000,
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
    with col2:
        types_public = ['All public transportation', 'Bus', 'Ferry', 'Railway','Train']
        fig2 = go.Figure()
        if choice_selected1 == 'normal person':
            for item in types_public:
                fig2.add_trace(
                    go.Bar(
                        x=df.index,
                        y=df[item],
                        hovertemplate="%{y:.2f}",
                        name= f'{item}',
                ),
                )
            # fig2.update_layout(barmode="stack")
            fig2.update_layout(
                paper_bgcolor="#bcbcbc",
                plot_bgcolor="#f9e5e5",
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
            )
            )
            st.plotly_chart(fig2)
    
elif choice_selected1 == 'normal person' and choice_selected2 == 'percentage of people':
    left_column1, right_column1 = st.columns([1, 1])
    choice3 = ['All public transportation', 'Bus', 'Ferry', 'Railway', 'Train']
    choice_selected3 = left_column1.selectbox("Select the type of public transportration", choice3)
    df = percent_normal
    st.write(f'{style_title_graph}<p class="center-text bold-color-text">The percentage of people can access to public transportration in BMR during 2020</p>', unsafe_allow_html=True)
    # st.write(f'<p style="text-align: center;">The percentage of people can access to public transportration in BMR during 2020</p>', unsafe_allow_html=True)
    col3, col4 = st.columns([1, 1])
    with col3 :
        fig = go.Figure(
            go.Choroplethmapbox(
                geojson= geo,
                locations=df.index,
                featureidkey="properties.ADM1_EN",
                z=df[f'{choice_selected3}'],
                colorscale="sunsetdark",
                # zmin=0,
                # zmax=500000,
                marker_opacity=0.5,
                marker_line_width=0,
            )
        )
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=8.2,
            mapbox_center={"lat": 13.72917, "lon": 100.52389},
            # width=1200,
            # height=800,
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
        
    with col4:
        fig2 = go.Figure()
        if choice_selected1 == 'normal person':
            for item in choice3:
                fig2.add_trace(
                    go.Bar(
                        x=df.index,
                        y=df[item],
                        hovertemplate="%{y:.2f}",
                        name= f'{item}',
                ),
                )
            # fig2.update_layout(barmode="stack")
            fig2.update_layout(
                paper_bgcolor="#bcbcbc",
                plot_bgcolor="#f9e5e5",
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
            )
            )
            st.plotly_chart(fig2)

elif choice_selected1 == 'disabled person' and choice_selected2 == 'number of people':
    left_column1, right_column1 = st.columns([1, 1])
    choice3 = ['All public transportation', 'Bus','Railway']
    choice_selected3 = left_column1.selectbox("Select the type of public transportration", choice3)
    df = number_dis
    st.write(f'{style_title_graph}<p class="center-text bold-color-text">The number of people with disable can access to public transportration in BMR during 2020</p>', unsafe_allow_html=True)
    col5, col6 = st.columns([1, 1])
    with col5:
        fig = go.Figure(
            go.Choroplethmapbox(
                geojson= geo,
                locations=df.index,
                featureidkey="properties.ADM1_EN",
                z=df[f'{choice_selected3}'],
                colorscale="sunsetdark",
                # zmin=0,
                # zmax=500000,
                marker_opacity=0.5,
                marker_line_width=0,
            )
        )
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=8.2,
            mapbox_center={"lat": 13.72917, "lon": 100.52389},
            # width=1200,
            # height=800,
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
    with col6:
        types_public = ['All public transportation', 'Bus', 'Railway']
        fig2 = go.Figure()
        if choice_selected1 == 'disabled person':
            for item in types_public:
                fig2.add_trace(
                    go.Bar(
                        x=df.index,
                        y=df[item],
                        hovertemplate="%{y:.2f}",
                        name= f'{item}',
                ),
                )
            # fig2.update_layout(barmode="stack")
            fig2.update_layout(
                paper_bgcolor="#bcbcbc",
                plot_bgcolor="#f9e5e5",
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
            )
            )
            st.plotly_chart(fig2)
elif choice_selected1 == 'disabled person' and choice_selected2 == 'percentage of people':
    left_column1, right_column1 = st.columns([1, 1])
    choice3 = ['All public transportation', 'Bus', 'Railway']
    choice_selected3 = left_column1.selectbox("Select the type of public transportration", choice3)
    df = percent_dis
    st.write('The percentage of people with disable can access to public transportration in BMR during 2020')
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson= geo,
            locations=df.index,
            featureidkey="properties.ADM1_EN",
            z=df[f'{choice_selected3}'],
            colorscale="sunsetdark",
            # zmin=0,
            # zmax=500000,
            marker_opacity=0.5,
            marker_line_width=0,
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=8.2,
        mapbox_center={"lat": 13.72917, "lon": 100.52389},
        width=1200,
        height=800,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)

