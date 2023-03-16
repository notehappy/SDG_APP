# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:44:38 2023

@author: Labtop
"""
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide", page_title='Home Page', page_icon=":mortar_board:")
st.sidebar.markdown("Home Page")

# =============================================================================
# Banner and Title
# =============================================================================
image = r'Image/banner.png'
st.image(image)

# =============================================================================
# General Imformation
# =============================================================================

# Set page title
st.title("Application of Big Earth Data in Support of Sustainable Development Goals in Thailand")

# Add subheader for general information section
st.subheader("General Information")

# Add info-graphic
st.image(r'Image/Info_graphic_project.png', caption = 'Info graphicd of the main project')

# Write project name
st.write("- **Project Name:** Application of Big Earth Data in Support of the Sustainable Development Goals in Thailand")

# Write project supporter
st.write("- **Supported By:** National Research Council of Thailand (NRCT)")

# Add subheader for sub-projects section
st.subheader("Sub-Projects")

# Write sub-projects list
st.write("1. Assessment of SDGs for Coastal Environment")
st.write("2. Assessment of SDGs for Urban Settlement")

# Add subheader for important keywords section
st.subheader("Important Keywords")

# Write important keywords list with highlighted text color
st.write("- <span style='color:red'>SDG Indicators Accountability</span>", unsafe_allow_html=True)
st.write("- <span style='color:red'>Big Earth Data</span>", unsafe_allow_html=True)
st.write("- <span style='color:red'>Traditional and Big Data Ecosystem Integration</span>", unsafe_allow_html=True)
st.write("- <span style='color:red'>Policy and Governance for SDGs</span>", unsafe_allow_html=True)

# =============================================================================
# Researcher
# =============================================================================
st.subheader("Researcher")

# Ajarn Pong
col1, col2 = st.columns([1,4])
col1.image(r'Image/Ekbordinw.jpg', width=300)
col2.write('<span style="color:green; font-weight:bold">Associate Professor Dr. Ekebodin Winijkul</span>', unsafe_allow_html=True)
col2.write('Position: Program Director and Researcher in second subproject')
col2.write('Department of Energy, Environment and Climate Change')
col2.write('Asian Institue of Technology, Thailand')

# Ajarn Wenchao
col3, col4 = st.columns([1,4])
col3.image(r'Image/Wenchao.jpeg', width=300)
col4.write('<span style="color:green; font-weight:bold">Associate Professor Dr. Wenchao Xue</span>', unsafe_allow_html=True)
col4.write('Position: First subproject director')
col4.write('Department of Energy, Environment and Climate Change')
col4.write('Asian Institue of Technology, Thailand')

# Ajarn Virdis
col5, col6 = st.columns([1,4])
col5.image(r'Image/Virdis.jpeg', width=300)
col6.write('<span style="color:green; font-weight:bold">Associate Professor Dr. Salvatore G.P. Virdis</span>', unsafe_allow_html=True)
col6.write('Position: Researcher in first subproject')
col6.write('Department of Information & Communication Technologies')
col6.write('Asian Institue of Technology, Thailand')

# Ajarn Lai
col7, col8 = st.columns([1,4])
col7.image(r'Image/Lai.jpg', width=300)
col8.write('<span style="color:green; font-weight:bold">Assisstant Professor Dr. Thi Phouc Lai Nguyen</span>', unsafe_allow_html=True)
col8.write('Position: Second subproject  director')
col8.write('Department of Development & Sustainability')
col8.write('Asian Institue of Technology, Thailand')

# Pongsakon
col9, col10 = st.columns([1,4])
col9.image(r'Image/Pongsakon.jpg', width=300)
col10.write('<span style="color:green; font-weight:bold">Mr. Pongsakon Punpukdee</span>', unsafe_allow_html=True)
col10.write('Position: Researcher')
col10.write('Department of Energy, Environment and Climate Change')
col10.write('Asian Institue of Technology, Thailand')


st.caption('For more information and details contact: Ekbordinw@ait.asia or pongsakon@ait.aisa')