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
st.title("PM2.5 concentration in Thailand using PM2.5 model of study")

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