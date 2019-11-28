#from flask import Flask
import flask
import dash
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

#colors = {
#    'background': '#1e2130',
#   'text': '#7FDBFF'
#}
#df = pd.read_excel('example7.xlsx')

@app.route('/test/')
def test():
    #external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app1 = dash.Dash(__name__, server = app, url_base_pathname='/dashboard/')
    dash_app1.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
    
    
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
