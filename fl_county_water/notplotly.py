import json
import pandas as pd
import requests
import plotly.express as px

counties = json.load(open("shape_files/fl_counties.geojson", 'r'))
df = pd.read_csv('shape_files/counties_plotly.csv')

myfile = "shape_files/fl_counties.geojson"
# open file for read-only
florida = open(myfile)
# read JSON format
florida_data = json.load(florida)

fig = px.choropleth(df, geojson=florida_data, locations='id', color='pct_bad',
                    featureidkey="properties.GEOID",
                    color_continuous_scale="algae",
                    range_color=(0, 15),
                    hover_name="county",
                    labels={'pct_bad':'Percent of wells over N limit', 'id':'County ID'}
                    )
fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

fig.write_html("plotly_countywells.html", include_plotlyjs="cdn")
