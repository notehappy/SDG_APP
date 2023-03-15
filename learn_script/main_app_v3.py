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

# =============================================================================
# Setting Image of AIT
# =============================================================================

image = Image.open(r'Image/AIT_logo.png')
st.image(image, width=400)
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
st.write("* The researchers responsible for Indicator 11.6.2 were Associate Professor Dr. Ekebodin Winijkul and Mr. Pongsakorn Phanphakdee.")

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
left_column, right_column = st.columns([1, 1])
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
    paper_bgcolor="#bcbcbc",
    plot_bgcolor="#f9e5e5",
    width=800,
    height=600,
    title=f"An assessment of Thailand was conducting using the model developing of this study.",
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
    paper_bgcolor="#bcbcbc",
    plot_bgcolor="#f9e5e5",
    width=800,
    height=600,
    title=f"An assessment of Thailand was conducting using the model developing of this study.",
    margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(fig2)
