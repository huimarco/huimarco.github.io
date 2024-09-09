import plotly.express as px
import pandas as pd

# Read data into pandas dataframe
df = pd.read_csv(r'files/visited_countries.csv')

# Define a custom color scale
color_scale = [
    [0, 'grey'],  # Zero values in grey
    [0.1, 'rgba(230, 230, 250, 0.6)'],  # Very light purple
    [0.5, 'rgba(138, 43, 226, 0.6)'],   # Medium purple
    [1, 'rgba(75, 0, 130, 0.6)']        # Dark purple
]

# Create the choropleth map
fig = px.choropleth(
    df,
    locations='ISO-code',  # Column with ISO country codes
    color='Rating',        # Column to shade by
    hover_name='Country',  # Column to display on hover
    hover_data={'ISO-code': False, 'Rating': False},  # Exclude ISO code and rating
    projection='equirectangular',  # 2D flat map projection
    color_continuous_scale= color_scale  # Apply the custom color scale
)

# Customize the layout
fig.update_layout(
    paper_bgcolor='rgb(30,30,30)',  # Dark grey background
    geo=dict(
        bgcolor='rgb(30,30,30)',  # Dark grey for map background
        showframe=False,  # Remove frame around the map
        showcoastlines=False,  # Remove coastlines
        projection_scale=1.2,  # Zoom into the map
        showcountries=True,  # Show country borders
        countrywidth=0.5  # Thickness of the country borders
    ),
    coloraxis_showscale=False,  # Remove color legend/scale
    autosize=False,  # Disable autosizing
    width=1000,  # Fixed width of the map window
    height=600,  # Fixed height of the map window
    margin=dict(l=0, r=0, t=0, b=0),  # Minimize margins
    uirevision='constant'  # Disable dynamic changes on user interaction
)

# Set the map as a rectangle window with no zoom interaction
fig.update_geos(
    fitbounds='locations',  # Fit the map to the country locations
    visible=False  # Disable all map elements except the countries
)

# Save the figure as an HTML file
fig.write_html('visited_countries_plot.html')