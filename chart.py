import json

import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import sys
import re

import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px

class GraphDash:
  def __init__(self, dash_app):
    super().__init__()
    self.dash_app = dash_app
  
    #apple data
    with open(sys.path[0]+'/newcrawler/newcrawler/apple.json', 'r') as file:
      json_data = json.load(file)
    data_apple = json_data

    #backmarket data
    with open(sys.path[0]+'/newcrawler/newcrawler/back_market.json', 'r') as file_bm:
      bm_data = json.load(file_bm)
    data_back_market = bm_data

    #all data
    dataframe=[]
    for i in data_apple:
      dataframe.append(i)
    for i in data_back_market:
      dataframe.append(i)
    
    #stockage list for dropdown
    stockage_list=[]
    for e in data_apple:
      stockage_list.append(e['stockage'])
    stockage_list=set(stockage_list)

    apple_price_fig = go.Figure()

    self.dash_app.layout = html.Div([
      html.P("Sélectionnez un produit", style={"font-family":"Arial"}),
      dcc.Dropdown(
            id='product_select',
            options=[
              {'label': 'iMac', 'value': 'iMac'},
              {'label': 'iPad', 'value': 'iPad'},
              {'label': 'iPhone', 'value': 'iPhone'},
              {'label': 'MacBook', 'value': 'MacBook'},
            ],
            value='iPhone',
      ),
      html.P("Sélectionnez un stockage", style={"font-family":"Arial"}),
      dcc.Dropdown(
            id='stockage_select',
            options=[{'label': i, 'value': i} for i in stockage_list],
      ),
      dcc.Graph(
            id='apple_fig',
            figure=apple_price_fig,
          ),
    ])

    @self.dash_app.callback(
      dash.dependencies.Output(component_id='apple_fig', component_property='figure'),
      [dash.dependencies.Input(component_id='product_select', component_property='value'),
      dash.dependencies.Input(component_id='stockage_select',component_property='value')]
      )
    def update_output(input_value,stockage_value):

      title_apple=[]
      currentPrice_apple=[]
      stockage_apple=[]
      site_apple=[]
      for i in data_apple:
        if(i['type']==input_value):
          if(i['stockage']==stockage_value):
            title_apple.append(i['title'])
            currentPrice_apple.append(i['currentPrice'][:-4])
            stockage_apple.append(i['stockage'])
            site_apple.append(i['stockage'])

      title_backmarket=[]
      currentPrice_backmarket=[]
      stockage_backmarket=[]
      site_backmarket=[]
      for i in data_back_market:
        if(i['type']==input_value):
          if(i['stockage']==int(stockage_value[:-3])):
            title_backmarket.append(i['title'])
            currentPrice_backmarket.append(i['currentPrice'][:-4])
            stockage_backmarket.append(i['stockage'])
            site_backmarket.append(i['stockage'])

      apple_price_fig=go.Figure()
      apple_price_fig.add_trace(
        go.Bar(
          x=title_apple,
          y=currentPrice_apple,
          marker_color='rgb(55, 83, 109)',
          name='Apple',
        )
      )

      apple_price_fig.add_trace(
        go.Bar(
          x=title_backmarket,
          y=currentPrice_backmarket,
          marker_color='rgb(26, 118, 255)',
          name='Backmarket',
        )
      )
      apple_price_fig.update_layout(
        yaxis=dict(
          title='Prix du produit en €'
        )
      )

      return apple_price_fig


# if __name__ == '__main__':
#   app = dash.Dash(__name__)
#   app.run_server(debug=True)