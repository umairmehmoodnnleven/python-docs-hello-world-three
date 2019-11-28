#from flask import Flask
import flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

app = flask.Flask(__name__)
#dash_app1 = Dash(__name__, server = app, url_base_pathname='/dashboard/')
#dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])

@app.route("/")
def hello():
    return "Hello World How are you doing? Test 1 2 3!"

colors = {
    'background': '#1e2130',
    'text': '#7FDBFF'
}

@app.route('/test/')
def test():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app1 = Dash(__name__, server = app, external_stylesheets = external_stylesheets, url_base_pathname='/dashboard/')
    dash_app1.layout = html.Div(style={'backgroundColor': colors['background']}, children =[
    html.H1("SII-sensitivities", style={"fontWeight": "bold", "textAlign": "center", 'color' : 'orange'}),
    
    html.Div([
        html.Div([
        html.Div([html.Div([dcc.Dropdown(id='product-selected1',
                                         options=[{'label': i.title(), 'value': i} for i in df.Scenario.unique()],
                                         value="Equity -25% MTM")], className="six columns",
                           style={"width": "40%", "float": "right"}),
                  html.Div([dcc.Dropdown(id='product-selected2',
                                         options=[{'label': i.title(), 'value': i} for i in df.Period.unique()],
                                         value='2019 Q1')], className="six columns", style={"width": "40%", "float": "left"}),
                  ], className="row", style={"padding": 50, "width": "60%", "margin-left": "auto", "margin-right": "auto"}),
        dcc.Graph(id='my-graph')
        ],className = 'eight columns'),
        
        
        html.Div(
            id="card-2",
            children=[
                html.P("Current SII-ratio", style={"textAlign": "center", 'color' : 'orange'}),
                daq.Gauge(
                    id="progress-gauge",
                    max=300,
                    min=0,
                    style={"textAlign": "center"},
                    value = 211,
                    showCurrentValue=True,  # default size 200 pixel
                    color = 'orange',),],className = 'four columns', style = {'margin-top':200}),
    ],className = 'row')
         
    # dcc.Link('Go to Source Code', href='{}/code'.format(app_name))
], className="row")
    
    @dash_app1.callback(
        dash.dependencies.Output('my-graph', 'figure'),
        [dash.dependencies.Input('product-selected1', 'value'),
        dash.dependencies.Input('product-selected2', 'value')])
    def update_graph(selected_product1, selected_product2):
        #dff = df[(df[selected_product1] >= 2) & (df[selected_product2] >= 2)]
        df1 = df[((df.Period == selected_product2))]
        df2 = df1[((df1.Scenario == 'Reported figures'))]
        df3 = df1[((df1.Scenario == selected_product1))]
        text = [int(df2['SII-ratio'].values[0]*100), int(df3['SII-ratio'].values[0]*100)]
        dff = pd.concat([df2, df3])
        trace1 = go.Bar(x=dff['Scenario'], y=dff['EOF'], name='EOF', )
        trace2 = go.Bar(x=dff['Scenario'], y=dff['SCR'], name='SCR', )

        return {
            'data': [trace1, trace2],
            'layout': go.Layout(title=  f'SII-ratio changes from {text[0]}% to {text[1]}%',
                                colorway=["#EF963B", "#EF533B"], hovermode="closest",
                                plot_bgcolor = colors['background'],
                                paper_bgcolor = colors['background'],
                                font = {'color' : 'orange'},
                                xaxis={'title': "Scenario", 'titlefont': {'color': 'orange', 'size': 14},
                                       'tickfont': {'size': 9, 'color': 'orange'}},
                                yaxis={'title': "EUR (million)", 'titlefont': {'color': 'orange', 'size': 14, },
                                       'tickfont': {'color': 'orange'}})}
    
    
    return dash_app1

@app.route('/test/')
def render_dashboard():
    return flask.redirect('/dashboard/')

#from dash import Dash
#from werkzeug.wsgi import DispatcherMiddleware
#import flask
#from werkzeug.serving import run_simple
#import dash_html_components as html

#server = flask.Flask(__name__)
#dash_app1 = Dash(__name__, server = app, url_base_pathname='/dashboard/' )
#dash_app2 = Dash(__name__, server = server, url_base_pathname='/reports/')
#dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
#dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])
#@server.route('/')
#@server.route('/hello/')
#def hello():
#    return 'hello world!'

#@app.route('/dash1/')
#def render_dashboard():
#    return flask.redirect('/dashboard/')


#@server.route('/reports/')
#def render_reports():
#    return flask.redirect('/dash2/')

#app = DispatcherMiddleware(server, {
#    '/dash1/': dash_app1.server,
#    '/dash2/': dash_app2.server
#})

#if __name__ == '__main__':
#    server.run()
    #run_simple(application= app, use_reloader=True, use_debugger=True)
