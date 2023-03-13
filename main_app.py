import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
st.set_page_config(layout ="wide")
json1 = fr"D:\2021_DataScience\2023_streamlit\SDG_app\Data\tha_admbnda_adm1_rtsd_201902_WGS.json"
# Add title and header
st.title("Renewable Energy Production in Switzerland")
st.header("Energy Production by Cantons (MWH) ")
m = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name="Light Map",
               zoom_start=5, attr="My Data attribution")

df = pd.read_excel(r'D:\2021_DataScience\2023_streamlit\SDG_app\Data\sdg_monthly_TH(pro).xlsx')

# choice = ['2018-02-01 00:00:00', '2018-03-01 00:00:00']
# choice_selected = st.selectbox("Select choice", choice)

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=df,
    columns=["ADM1_EN",'test'],
    key_on="feature.properties.ADM1_EN",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name='2018-02-01 00:00:00'
).add_to(m)

folium.features.GeoJson(json1,
                        name="ADM1_EN", popup=folium.features.GeoJsonPopup(fields=["ADM1_EN"])).add_to(m)

folium_static(m, width=1600, height=950)