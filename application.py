#from flask import Flask
import flask
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

app = flask.Flask(__name__)
#dash_app1 = Dash(__name__, server = app, url_base_pathname='/dashboard/')
#dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
w_dir = os.getcwd()# get current working directory

@app.route("/")
def hello():
    return "Hello World How are you doing? Test 1 2 3!"

colors = {
    'background': '#1e2130',
   'text': '#7FDBFF'
}

df = pd.DataFrame( {'Period': {0: '2019 Q2', 1: '2019 Q2', 2: '2019 Q2', 3: '2019 Q2', 4: '2019 Q2', 5: '2019 Q2', 6: '2019 Q2', 7: '2019 Q2', 8: '2019 Q2', 9: '2019 Q2', 10: '2019 Q2', 11: '2019 Q2', 12: '2019 Q2', 13: '2019 Q2', 14: '2019 Q2', 15: '2019 Q2', 16: '2019 Q2', 17: '2019 Q2', 18: '2019 Q2', 19: '2019 Q2', 20: '2019 Q2', 21: '2019 Q1', 22: '2019 Q1', 23: '2019 Q1', 24: '2019 Q1', 25: '2019 Q1', 26: '2019 Q1', 27: '2019 Q1', 28: '2019 Q1', 29: '2019 Q1', 30: '2019 Q1', 31: '2019 Q1', 32: '2019 Q1', 33: '2019 Q1', 34: '2019 Q1', 35: '2019 Q1', 36: '2019 Q1', 37: '2019 Q1', 38: '2019 Q1', 39: '2019 Q1', 40: '2019 Q1', 41: '2019 Q1'},
                    'Scenario': {0: 'Reported figures', 1: 'Equity -25% MTM', 2: 'Real estate -25% MTM', 3: 'Mortgage spread +50bps', 4: 'Corporate bond spread +50bps', 5: 'Sovereign bond spread +50bps', 6: 'UFR set to 3.75%', 7: 'UFR set to 3.60%', 8: 'Last Liquid Point set to 30 years', 9: 'Interest Rate +1bps', 10: 'Interest Rate +10bps', 11: 'Interest Rate +25bps', 12: 'Interest Rate +50bps', 13: 'Interest Rate +75bps', 14: 'Interest Rate +100bps', 15: 'Interest Rate -1bps', 16: 'Interest Rate -10bps', 17: 'Interest Rate -25bps', 18: 'Interest Rate -50bps', 19: 'Interest Rate -75bps', 20: 'Interest Rate -100bps', 21: 'Reported figures', 22: 'Equity -25% MTM', 23: 'Real estate -25% MTM', 24: 'Mortgage spread +50bps', 25: 'Corporate bond spread +50bps', 26: 'Sovereign bond spread +50bps', 27: 'UFR set to 3.75%', 28: 'UFR set to 3.60%', 29: 'Last Liquid Point set to 30 years', 30: 'Interest Rate +1bps', 31: 'Interest Rate +10bps', 32: 'Interest Rate +25bps', 33: 'Interest Rate +50bps', 34: 'Interest Rate +75bps', 35: 'Interest Rate +100bps', 36: 'Interest Rate -1bps', 37: 'Interest Rate -10bps', 38: 'Interest Rate -25bps', 39: 'Interest Rate -50bps', 40: 'Interest Rate -75bps', 41: 'Interest Rate -100bps'},
                    'Name': {0: 'Reported', 1: 'EQ_Down25', 2: 'RE_Down10', 3: 'CS_corp50_Mortg', 4: 'CS_corp50_Excl mortg', 5: 'CS_gov50', 6: 'UFR_375', 7: 'UFR_360', 8: 'LLP_30', 9: 'IR_Up1_fullcurve', 10: 'IR_Up10_fullcurve', 11: 'IR_Up25_fullcurve', 12: 'IR_Up50', 13: 'IR_Up75_fullcurve', 14: 'IR_Up100_fullcurve', 15: 'IR_Down1_fullcurve', 16: 'IR_Down10_fullcurve', 17: 'IR_Down25_fullcurve', 18: 'IR_Down50', 19: 'IR_Down75_fullcurve', 20: 'IR_Down100_fullcurve', 21: 'Reported', 22: 'EQ_Down25', 23: 'RE_Down10', 24: 'CS_corp50_Mortg', 25: 'CS_corp50_Excl mortg', 26: 'CS_gov50', 27: 'UFR_375', 28: 'UFR_360', 29: 'LLP_30', 30: 'IR_Up1_fullcurve', 31: 'IR_Up10_fullcurve', 32: 'IR_Up25_fullcurve', 33: 'IR_Up50', 34: 'IR_Up75_fullcurve', 35: 'IR_Up100_fullcurve', 36: 'IR_Down1_fullcurve', 37: 'IR_Down10_fullcurve', 38: 'IR_Down25_fullcurve', 39: 'IR_Down50', 40: 'IR_Down75_fullcurve', 41: 'IR_Down100_fullcurve'},
                    'Unnamed: 3': {0: 'Reported@2019 Q2', 1: 'EQ_Down25@2019 Q2', 2: 'RE_Down10@2019 Q2', 3: 'CS_corp50_Mortg@2019 Q2', 4: 'CS_corp50_Excl mortg@2019 Q2', 5: 'CS_gov50@2019 Q2', 6: 'UFR_375@2019 Q2', 7: 'UFR_360@2019 Q2', 8: 'LLP_30@2019 Q2', 9: 'IR_Up1_fullcurve@2019 Q2', 10: 'IR_Up10_fullcurve@2019 Q2', 11: 'IR_Up25_fullcurve@2019 Q2', 12: 'IR_Up50@2019 Q2', 13: 'IR_Up75_fullcurve@2019 Q2', 14: 'IR_Up100_fullcurve@2019 Q2', 15: 'IR_Down1_fullcurve@2019 Q2', 16: 'IR_Down10_fullcurve@2019 Q2', 17: 'IR_Down25_fullcurve@2019 Q2', 18: 'IR_Down50@2019 Q2', 19: 'IR_Down75_fullcurve@2019 Q2', 20: 'IR_Down100_fullcurve@2019 Q2', 21: 'Reported@2019 Q1', 22: 'EQ_Down25@2019 Q1', 23: 'RE_Down10@2019 Q1', 24: 'CS_corp50_Mortg@2019 Q1', 25: 'CS_corp50_Excl mortg@2019 Q1', 26: 'CS_gov50@2019 Q1', 27: 'UFR_375@2019 Q1', 28: 'UFR_360@2019 Q1', 29: 'LLP_30@2019 Q1', 30: 'IR_Up1_fullcurve@2019 Q1', 31: 'IR_Up10_fullcurve@2019 Q1', 32: 'IR_Up25_fullcurve@2019 Q1', 33: 'IR_Up50@2019 Q1', 34: 'IR_Up75_fullcurve@2019 Q1', 35: 'IR_Up100_fullcurve@2019 Q1', 36: 'IR_Down1_fullcurve@2019 Q1', 37: 'IR_Down10_fullcurve@2019 Q1', 38: 'IR_Down25_fullcurve@2019 Q1', 39: 'IR_Down50@2019 Q1', 40: 'IR_Down75_fullcurve@2019 Q1', 41: 'IR_Down100_fullcurve@2019 Q1'},
                    'EOF': {0: 12305.432899449515, 1: 11281.378585638829, 2: 11591.823430270368, 3: 11484.332401284057, 4: 13258.319948713253, 5: 10748.644204347645, 6: 11994.672153975063, 7: 11664.275643910321, 8: 7081.4114857288914, 9: 12290.549951547569, 10: 12119.711018883325, 11: 11843.87999860886, 12: 11442.354474451909, 13: 11105.314690002719, 14: 10827.220141896281, 15: 12320.859491104784, 16: 12462.411871229149, 17: 12717.387516780731, 18: 13199.563587065257, 19: 13760.728226547561, 20: 14410.359626625061, 21: 12305.432899449515, 22: 11281.378585638829, 23: 11591.823430270368, 24: 11484.332401284057, 25: 13258.319948713253, 26: 10748.644204347645, 27: 11994.672153975063, 28: 11664.275643910321, 29: 7081.4114857288914, 30: 12290.549951547569, 31: 12119.711018883325, 32: 11843.87999860886, 33: 11442.354474451909, 34: 11105.314690002719, 35: 10827.220141896281, 36: 12320.859491104784, 37: 12462.411871229149, 38: 12717.387516780731, 39: 13199.563587065257, 40: 13760.728226547561, 41: 14410.359626625061}, 
                    'SCR': {0: 5804.579427358105, 1: 5721.4459556556058, 2: 5801.559593825823, 3: 5794.8612456170276, 4: 5716.8822454406309, 5: 5687.4532995609306, 6: 5834.6268037881136, 7: 5868.5266874616182, 8: 6834.1189164091002, 9: 5793.4247209208115, 10: 5698.8749271187471, 11: 5556.1240418481348, 12: 5338.0138437103269, 13: 5134.1694669961253, 14: 4954.132433900927, 15: 5815.4768171395381, 16: 5917.2482053481526, 17: 6089.6190116772541, 18: 6396.1458193823064, 19: 6740.5158277942755, 20: 7123.4183814338885, 21: 5804.579427358105, 22: 5721.4459556556058, 23: 5801.559593825823, 24: 5794.8612456170276, 25: 5716.8822454406309, 26: 5687.4532995609306, 27: 5834.6268037881136, 28: 5868.5266874616182, 29: 6834.1189164091002, 30: 5793.4247209208115, 31: 5698.8749271187471, 32: 5556.1240418481348, 33: 5338.0138437103269, 34: 5134.1694669961253, 35: 4954.132433900927, 36: 5815.4768171395381, 37: 5917.2482053481526, 38: 6089.6190116772541, 39: 6396.1458193823064, 40: 6740.5158277942755, 41: 7123.4183814338885},
                    'SII-ratio': {0: 2.119952539791536, 1: 1.9717705407122255, 2: 1.9980529791690325, 3: 1.9818131814580184, 4: 2.3191521846172578, 5: 1.8898870264442325, 6: 2.0557736693951973, 7: 1.987598636780777, 8: 1.0361849965364267, 9: 2.1214653755946449, 10: 2.1266848586569775, 11: 2.1316802701671196, 12: 2.1435602846804533, 13: 2.163020671871231, 14: 2.1854926743189291, 15: 2.1186327241117011, 16: 2.1061161267437316, 17: 2.0883716193729502, 18: 2.0636745877597855, 19: 2.0414948318651951, 20: 2.0229556731054128, 21: 2.119952539791536, 22: 1.9717705407122255, 23: 1.9980529791690325, 24: 1.9818131814580184, 25: 2.3191521846172578, 26: 1.8898870264442325, 27: 2.0557736693951973, 28: 1.987598636780777, 29: 1.0361849965364267, 30: 2.1214653755946449, 31: 2.1266848586569775, 32: 2.1316802701671196, 33: 2.1435602846804533, 34: 2.163020671871231, 35: 2.1854926743189291, 36: 2.1186327241117011, 37: 2.1061161267437316, 38: 2.0883716193729502, 39: 2.0636745877597855, 40: 2.0414948318651951, 41: 2.0229556731054128}, 
                    'OF Expl.': {0: float('nan'), 1: 'Own Funds decrease due to lower market value of equities', 2: 'Own Funds decrease due to lower market value of real estate', 3: 'Own Funds decrease due to lower market value of mortgages', 4: 'Own Funds decrease due to lower market value of corporate bonds', 5: 'Own Funds decrease due to lower market value of sovereign bonds', 6: 'Own Funds decrease due to high valuation of Liabilities', 7: 'Own Funds decrease due to high valuation of Liabilities', 8: 'Own Funds decrease due to high valuation of Liabilities', 9: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 10: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 11: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 12: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 13: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 14: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 15: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 16: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 17: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 18: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 19: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 20: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 21: float('nan'), 22: 'Own Funds decrease due to lower market value of equities', 23: 'Own Funds decrease due to lower market value of real estate', 24: 'Own Funds decrease due to lower market value of mortgages', 25: 'Own Funds decrease due to lower market value of corporate bonds', 26: 'Own Funds decrease due to lower market value of sovereign bonds', 27: 'Own Funds decrease due to high valuation of Liabilities', 28: 'Own Funds decrease due to high valuation of Liabilities', 29: 'Own Funds decrease due to high valuation of Liabilities', 30: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 31: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 32: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 33: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 34: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 35: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 36: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 37: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 38: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 39: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 40: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 41: 'Own Funds decrease due to lower valuation of assets and liabilities. '},
                    'SCR Expl.': {0: float('nan'), 1: 'SCR decreases as less capital is required due to decreased equity exposure ', 2: 'SCR decreases as less capital is required due to decreased real estate exposure ', 3: 'SCR decreases due to decreased exposure to mortgages', 4: 'SCR decreases due to decreased exposure to corporate bonds', 5: 'SCR decreases due to decreased exposure to sovereign bonds', 6: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 7: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 8: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 9: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 10: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 11: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 12: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 13: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 14: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 15: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 16: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 17: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 18: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 19: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 20: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 21: float('nan'), 22: 'SCR decreases as less capital is required due to decreased equity exposure ', 23: 'SCR decreases as less capital is required due to decreased real estate exposure ', 24: 'SCR decreases due to decreased exposure to mortgages', 25: 'SCR decreases due to decreased exposure to corporate bonds', 26: 'SCR decreases due to decreased exposure to sovereign bonds', 27: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 28: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 29: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 30: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 31: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 32: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 33: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 34: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 35: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 36: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 37: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 38: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 39: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 40: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 41: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk'}} ) 

@app.route('/test/')
def test():
    #external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    #df = pd.read_excel(w_dir + 'example7.xlsx')
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
