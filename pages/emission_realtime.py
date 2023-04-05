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
st.title("PM2.5 concentration in Thailand using PM2.5 model of study")
