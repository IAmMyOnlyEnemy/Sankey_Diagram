# Get this figure: fig = py.get_figure("https://plotly.com/~alishobeiri/1577/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~alishobeiri/1577/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="plot from API (648)", fileopt="extend")

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import chart_studio.plotly as cs
from plotly.graph_objs import *
#cs.sign_in('username', 'api_key')
trace1 = {
  "link": {
    "label": ["stream 1", "", "", "", 
              "stream 1", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "stream 1", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "Old generation plant (made-up)", "New generation plant (made-up)", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", "", "", 
              "", "", ""], 
    "value": [124.729, 0.597, 26.862, 280.322, 
              81.144, 35, 35, 11.606, 63.965, 
              75.571, 10.639, 22.505, 46.184, 
              104.453, 113.726, 27.14, 342.165, 
              37.797, 4.412, 40.858, 56.691, 
              7.863, 90.008, 93.494, 40.719, 
              82.233, 0.129, 1.401, 151.891, 
              2.096, 48.58, 7.013, 20.897, 
              6.242, 20.897, 6.995, 121.066, 
              128.69, 135.835, 14.458, 206.267, 
              3.64, 33.218, 4.413, 14.375, 
              122.952, 500, 139.978, 504.287, 
              107.703, 611.99, 56.587, 77.81, 
              193.026, 70.672, 59.901, 19.263, 
              19.263, 59.901, 0.882, 400.12, 
              46.477, 525.531, 787.129, 79.329, 
              9.452, 182.01, 19.013, 289.366, 
              100, 100], 
    "source": [0, 1, 1, 1, 1, 6, 7, 8, 10, 9, 
              11, 11, 11, 15, 15, 15, 15, 15, 
              15, 15, 15, 15, 15, 15, 23, 25, 
              5, 5, 5, 5, 5, 27, 17, 17, 28, 
              29, 2, 2, 2, 2, 2, 2, 2, 2, 34, 
              24, 35, 35, 36, 38, 37, 39, 39, 
              40, 40, 41, 42, 43, 43, 4, 4, 4, 
              26, 26, 26, 44, 45, 46, 47, 35, 35], 
    "target": [1, 2, 3, 4, 5, 2, 4, 9, 9, 4, 
              12, 13, 14, 16, 14, 17, 12, 18, 19, 13, 
              3, 20, 21, 22, 24, 24, 13, 3, 26, 19, 
              12, 15, 28, 3, 18, 15, 12, 30, 18, 31, 
              32, 19, 33, 20, 1, 5, 26, 26, 37, 37, 2, 4, 1, 14, 13, 15, 14, 42, 41, 19, 26, 12, 15, 3, 11, 15, 1, 15, 15, 26, 26]
  }, 
  "node": {
    "pad": 10, 
    "line": {
      "color": "black", 
      "width": 0.5
    }, 
    "color": ["rgba(31, 119, 180, 0.8)", 
              "rgba(255, 127, 14, 0.8)", 
              "rgba(44, 160, 44, 0.8)", 
              "rgba(214, 39, 40, 0.8)", 
              "rgba(148, 103, 189, 0.8)", 
              "rgba(140, 86, 75, 0.8)", 
              "rgba(227, 119, 194, 0.8)", 
              "rgba(127, 127, 127, 0.8)", 
              "rgba(188, 189, 34, 0.8)", 
              "rgba(23, 190, 207, 0.8)", 
              "rgba(31, 119, 180, 0.8)", 
              "rgba(255, 127, 14, 0.8)", 
              "rgba(44, 160, 44, 0.8)", 
              "rgba(214, 39, 40, 0.8)", 
              "rgba(148, 103, 189, 0.8)", 
              "rgba(140, 86, 75, 0.8)", 
              "rgba(227, 119, 194, 0.8)", 
              "rgba(127, 127, 127, 0.8)", 
              "rgba(188, 189, 34, 0.8)", 
              "rgba(23, 190, 207, 0.8)", 
              "rgba(31, 119, 180, 0.8)", 
              "rgba(255, 127, 14, 0.8)", 
              "rgba(44, 160, 44, 0.8)", 
              "rgba(214, 39, 40, 0.8)", 
              "rgba(148, 103, 189, 0.8)", 
              "rgba(140, 86, 75, 0.8)", 
              "rgba(227, 119, 194, 0.8)", 
              "rgba(127, 127, 127, 0.8)", 
              "rgba(188, 189, 34, 0.8)", 
              "rgba(23, 190, 207, 0.8)", 
              "rgba(31, 119, 180, 0.8)", 
              "rgba(255, 127, 14, 0.8)", 
              "rgba(44, 160, 44, 0.8)", 
              "rgba(214, 39, 40, 0.8)", 
              "rgba(148, 103, 189, 0.8)", 
              "magenta", 
              "rgba(227, 119, 194, 0.8)", 
              "rgba(127, 127, 127, 0.8)", 
              "rgba(188, 189, 34, 0.8)", 
              "rgba(23, 190, 207, 0.8)", 
              "rgba(31, 119, 180, 0.8)", 
              "rgba(255, 127, 14, 0.8)", 
              "rgba(44, 160, 44, 0.8)", 
              "rgba(214, 39, 40, 0.8)", 
              "rgba(148, 103, 189, 0.8)", 
              "rgba(140, 86, 75, 0.8)", 
              "rgba(227, 119, 194, 0.8)", 
              "rgba(127, 127, 127, 0.8)"], 
    "label": ["Agricultural 'waste'",
              "Bio-conversion", 
              "Liquid", "Losses", 
              "Solid", 
              "Gas", 
              "Biofuel imports", 
              "Biomass imports", 
              "Coal imports", 
              "Coal", 
              "Coal reserves", 
              "District heating", 
              "Industry", 
              "Heating and cooling - commercial", 
              "Heating and cooling - homes", 
              "Electricity grid", 
              "Over generation / exports", 
              "H2 conversion", 
              "Road transport", 
              "Agriculture", 
              "Rail transport", 
              "Lighting & appliances - commercial", 
              "Lighting & appliances - homes", 
              "Gas imports", 
              "Ngas", 
              "Gas reserves", 
              "Thermal generation", 
              "Geothermal", 
              "H2", 
              "Hydro", 
              "International shipping", 
              "Domestic aviation", 
              "International aviation", 
              "National navigation", 
              "Marine algae", 
              "Nuclear", 
              "Oil imports", 
              "Oil", 
              "Oil reserves", 
              "Other waste", 
              "Pumped heat", 
              "Solar PV", 
              "Solar Thermal", 
              "Solar", 
              "Tidal", 
              "UK land based bioenergy", 
              "Wave", 
              "Wind"], 
    "thickness": 15
  }, 
  "type": "sankey", 
  "width": 1118, 
  "domain": {
    "x": [0, 1], 
    "y": [0, 1]
  }, 
  "height": 2500, 
  "orientation": "h", 
  "valueformat": ".0f", 
  "valuesuffix": "TWh"
}
data = Data([trace1])
layout = {
  "font": {"size": 10}, 
  "title": "Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>", 
  "height": 750, 
  "updatemenus": [
    {
      "y": 1, 
      "buttons": [
        {
          "args": ["paper_bgcolor", "white"], 
          "label": "Light", 
          "method": "relayout"
        }, 
        {
          "args": ["paper_bgcolor", "black"], 
          "label": "Dark", 
          "method": "relayout"
        }
      ]
    }, 
    {
      "y": 0.9, 
      "buttons": [
        {
          "args": ["node.thickness", 15], 
          "label": "Thick", 
          "method": "restyle"
        }, 
        {
          "args": ["node.thickness", 8], 
          "label": "Thin", 
          "method": "restyle"
        }
      ]
    }, 
    {
      "y": 0.8, 
      "buttons": [
        {
          "args": ["node.pad", 15], 
          "label": "Small gap", 
          "method": "restyle"
        }, 
        {
          "args": ["node.pad", 20], 
          "label": "Large gap", 
          "method": "restyle"
        }
      ]
    }, 
    {
      "y": 0.7, 
      "buttons": [
        {
          "args": ["arrangement", "snap"], 
          "label": "Snap", 
          "method": "restyle"
        }, 
        {
          "args": ["arrangement", "perpendicular"], 
          "label": "Perpendicular", 
          "method": "restyle"
        }, 
        {
          "args": ["arrangement", "freeform"], 
          "label": "Freeform", 
          "method": "restyle"
        }, 
        {
          "args": ["arrangement", "fixed"], 
          "label": "Fixed", 
          "method": "restyle"
        }
      ]
    }, 
    {
      "y": 0.6, 
      "buttons": [
        {
          "args": ["orientation", "h"], 
          "label": "Horizontal", 
          "method": "restyle"
        }, 
        {
          "args": ["orientation", "v"], 
          "label": "Vertical", 
          "method": "restyle"
        }
      ]
    }
  ]
}
fig = Figure(data=data, layout=layout)
plot_url = cs.plot(fig)