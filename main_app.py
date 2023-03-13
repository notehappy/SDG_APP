import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
json1 = r"Data/tha_admbnda_adm1_rtsd_201902_WGS.json"

m = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name="Light Map",
               zoom_start=5, attr="My Data attribution")

df = r"Data/sdg_monthly_TH(pro).csv"
df = pd.read_csv(df)

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

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=df,
    columns=["ADM1_EN",choice_selected],
    key_on="feature.properties.ADM1_EN",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name=choice_selected
).add_to(m)
folium.features.GeoJson(json1,
                        name="ADM1_EN", popup=folium.features.GeoJsonPopup(fields=["ADM1_EN"])).add_to(m)

folium_static(m, width=1600, height=950)