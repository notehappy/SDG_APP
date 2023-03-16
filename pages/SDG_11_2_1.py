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
json1 = "Data/6_provinces_WGS"
with open(json1) as response:
    geo = json.load(response)
