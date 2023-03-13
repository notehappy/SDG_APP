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

json1 = "Data/tha_admbnda_adm1_rtsd_201902_WGS.json"
with open(json1) as response:
    geo = json.load(response)

df = r"Data/sdg_monthly_TH(pro).csv"
df = pd.read_csv(df)

image = Image.open(r'Image/AIT_logo.png')
st.image(image, caption='Sunrise by the mountains', width=400)
st.title("An assessment of Thailand's progress towards achieving SDG indicator 11.6.2 for the period 2018 - 2021")
st.header("Spatial distribution of SDG 11.6.2 by monthly average and provinces in Thailand")



choice = ['February 2018', 'March 2018', 'April 2018', 'May 2018',
       'June 2018', 'July 2018', 'August 2018', 'September 2018',
       'October 2018', 'November 2018', 'December 2018', 'January 2019',
       'February 2019', 'March 2019', 'April 2019', 'May 2019', 'June 2019',
       'July 2019', 'August 2019', 'September 2019', 'October 2019',
       'November 2019', 'December 2019', 'January 2020', 'February 2020',
       'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020',
       'August 2020', 'September 2020', 'October 2020', 'November 2020',
       'December 2020', 'January 2021', 'February 2021', 'March 2021',
       'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021',
       'September 2021', 'October 2021', 'November 2021', 'December 2021']
choice_selected = st.selectbox("Select choice", choice)
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

