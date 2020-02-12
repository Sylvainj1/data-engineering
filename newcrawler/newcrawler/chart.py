import json

import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import sys
import re
import glob

with open(sys.path[0]+'/apple.json') as file:
  data_apple = json.load(file)

with open(sys.path[0]+'/back_market.json') as file:
  data_back_market = json.load(file)

dataframe=[]
for i in data_apple:
  dataframe.append(i)
for i in data_back_market:
  dataframe.append(i)

print(dataframe)
apple_price_fig = go.Figure()

app = dash.Dash(__name__)
app.layout = html.Div([
  html.P("Sélectionnez un produit", style={"font-family":"Arial"}),
  dcc.Dropdown(
        id='apple_select',
        options=[
          {'label': 'iMac', 'value': 'iMac'},
          {'label': 'iPad', 'value': 'iPad'},
          {'label': 'iPhone', 'value': 'iPhone'},
          {'label': 'MacBook', 'value': 'MacBook'},
        ],
        value='iPhone',
  ),
  dcc.Graph(
        id='apple_fig',
        figure=apple_price_fig,
      ),
])


@app.callback(
  dash.dependencies.Output('apple_fig', 'figure'),
  [dash.dependencies.Input('apple_select', 'value')])
def update_output(input_value):

  title=[]
  currentPrice=[]
  stockage=[]
  site=[]

  for i in dataframe:
    if(i['type']==input_value):
      title.append(i['title'])
      currentPrice.append(i['currentPrice'])
      stockage.append(i['stockage'])
      site.append(i['site'])


  apple_price_fig=go.Figure()
  apple_price_fig.add_trace(
    go.Bar(
      name='Apple',
      x= stockage,
      y=currentPrice,
      color=site,
      barmode='group',
    )
  )
  
  return apple_price_fig


if __name__ == '__main__':
  app.run_server(debug=True)