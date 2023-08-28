import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
from dash import dcc, html

file='document.xlsx'

df_s1=pd.read_excel(file,sheet_name="Document")

grp_data=df_s1.groupby(['Status']).size().reset_index(name='Count')

aut_count=grp_data[grp_data['Status']=='Authoring']
a=aut_count.columns.get_loc('Count')                    #Get column index value
val=aut_count.values[0][a]

# Create a donut chart using Plotly
fig_1 = px.pie(grp_data, values='Count', names='Status', hole=0.5, title='Status Distribution', hover_data=['Status'])
fig_1.update_traces(textinfo='percent+label',marker=dict(colors=['E6F69D', 'AADEA7', '64C2A6', '2D87BB']))

# Create Data card using plotty

fig_2 = go.Figure(go.Indicator(
    mode = "number",
    value = val,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "No of authoring"}))

# Create dash app

app=dash.Dash()
server=app.server

# Define the layout of the dashboard

app.layout = html.Div([
    html.H1("Department of technical communication dashboard"),
    
    html.Div([
        dcc.Graph(figure=fig_1)
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(figure=fig_2)
    ], style={'width': '49%', 'display': 'inline-block'}),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
