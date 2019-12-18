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
#dash_app1 = Dash(__name__, server = app, url_base_pathname='/')
#dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
w_dir = os.getcwd()# get current working directory

#@app.route("/")
#def hello():
#    return "Hello World How are you doing? Test 1 2 3!"

colors = {
    'background': '#1e2130',
   'text': '#7FDBFF'
}

df = pd.DataFrame( {'Period': {0: '2019 Q2', 1: '2019 Q2', 2: '2019 Q2', 3: '2019 Q2', 4: '2019 Q2', 5: '2019 Q2', 6: '2019 Q2', 7: '2019 Q2', 8: '2019 Q2', 9: '2019 Q2', 10: '2019 Q2', 11: '2019 Q2', 12: '2019 Q2', 13: '2019 Q2', 14: '2019 Q2', 15: '2019 Q2', 16: '2019 Q2', 17: '2019 Q2', 18: '2019 Q2', 19: '2019 Q2', 20: '2019 Q2', 21: '2019 Q1', 22: '2019 Q1', 23: '2019 Q1', 24: '2019 Q1', 25: '2019 Q1', 26: '2019 Q1', 27: '2019 Q1', 28: '2019 Q1', 29: '2019 Q1', 30: '2019 Q1', 31: '2019 Q1', 32: '2019 Q1', 33: '2019 Q1', 34: '2019 Q1', 35: '2019 Q1', 36: '2019 Q1', 37: '2019 Q1', 38: '2019 Q1', 39: '2019 Q1', 40: '2019 Q1', 41: '2019 Q1'},
                    'Scenario': {0: 'Reported figures', 1: 'Equity -25% MTM', 2: 'Real estate -25% MTM', 3: 'Mortgage spread +50bps', 4: 'Corporate bond spread +50bps', 5: 'Sovereign bond spread +50bps', 6: 'UFR set to 3.75%', 7: 'UFR set to 3.60%', 8: 'Last Liquid Point set to 30 years', 9: 'Interest Rate +1bps', 10: 'Interest Rate +10bps', 11: 'Interest Rate +25bps', 12: 'Interest Rate +50bps', 13: 'Interest Rate +75bps', 14: 'Interest Rate +100bps', 15: 'Interest Rate -1bps', 16: 'Interest Rate -10bps', 17: 'Interest Rate -25bps', 18: 'Interest Rate -50bps', 19: 'Interest Rate -75bps', 20: 'Interest Rate -100bps', 21: 'Reported figures', 22: 'Equity -25% MTM', 23: 'Real estate -25% MTM', 24: 'Mortgage spread +50bps', 25: 'Corporate bond spread +50bps', 26: 'Sovereign bond spread +50bps', 27: 'UFR set to 3.75%', 28: 'UFR set to 3.60%', 29: 'Last Liquid Point set to 30 years', 30: 'Interest Rate +1bps', 31: 'Interest Rate +10bps', 32: 'Interest Rate +25bps', 33: 'Interest Rate +50bps', 34: 'Interest Rate +75bps', 35: 'Interest Rate +100bps', 36: 'Interest Rate -1bps', 37: 'Interest Rate -10bps', 38: 'Interest Rate -25bps', 39: 'Interest Rate -50bps', 40: 'Interest Rate -75bps', 41: 'Interest Rate -100bps'},
                    'Name': {0: 'Reported', 1: 'EQ_Down25', 2: 'RE_Down10', 3: 'CS_corp50_Mortg', 4: 'CS_corp50_Excl mortg', 5: 'CS_gov50', 6: 'UFR_375', 7: 'UFR_360', 8: 'LLP_30', 9: 'IR_Up1_fullcurve', 10: 'IR_Up10_fullcurve', 11: 'IR_Up25_fullcurve', 12: 'IR_Up50', 13: 'IR_Up75_fullcurve', 14: 'IR_Up100_fullcurve', 15: 'IR_Down1_fullcurve', 16: 'IR_Down10_fullcurve', 17: 'IR_Down25_fullcurve', 18: 'IR_Down50', 19: 'IR_Down75_fullcurve', 20: 'IR_Down100_fullcurve', 21: 'Reported', 22: 'EQ_Down25', 23: 'RE_Down10', 24: 'CS_corp50_Mortg', 25: 'CS_corp50_Excl mortg', 26: 'CS_gov50', 27: 'UFR_375', 28: 'UFR_360', 29: 'LLP_30', 30: 'IR_Up1_fullcurve', 31: 'IR_Up10_fullcurve', 32: 'IR_Up25_fullcurve', 33: 'IR_Up50', 34: 'IR_Up75_fullcurve', 35: 'IR_Up100_fullcurve', 36: 'IR_Down1_fullcurve', 37: 'IR_Down10_fullcurve', 38: 'IR_Down25_fullcurve', 39: 'IR_Down50', 40: 'IR_Down75_fullcurve', 41: 'IR_Down100_fullcurve'},
                    'Unnamed: 3': {0: 'Reported@2019 Q2', 1: 'EQ_Down25@2019 Q2', 2: 'RE_Down10@2019 Q2', 3: 'CS_corp50_Mortg@2019 Q2', 4: 'CS_corp50_Excl mortg@2019 Q2', 5: 'CS_gov50@2019 Q2', 6: 'UFR_375@2019 Q2', 7: 'UFR_360@2019 Q2', 8: 'LLP_30@2019 Q2', 9: 'IR_Up1_fullcurve@2019 Q2', 10: 'IR_Up10_fullcurve@2019 Q2', 11: 'IR_Up25_fullcurve@2019 Q2', 12: 'IR_Up50@2019 Q2', 13: 'IR_Up75_fullcurve@2019 Q2', 14: 'IR_Up100_fullcurve@2019 Q2', 15: 'IR_Down1_fullcurve@2019 Q2', 16: 'IR_Down10_fullcurve@2019 Q2', 17: 'IR_Down25_fullcurve@2019 Q2', 18: 'IR_Down50@2019 Q2', 19: 'IR_Down75_fullcurve@2019 Q2', 20: 'IR_Down100_fullcurve@2019 Q2', 21: 'Reported@2019 Q1', 22: 'EQ_Down25@2019 Q1', 23: 'RE_Down10@2019 Q1', 24: 'CS_corp50_Mortg@2019 Q1', 25: 'CS_corp50_Excl mortg@2019 Q1', 26: 'CS_gov50@2019 Q1', 27: 'UFR_375@2019 Q1', 28: 'UFR_360@2019 Q1', 29: 'LLP_30@2019 Q1', 30: 'IR_Up1_fullcurve@2019 Q1', 31: 'IR_Up10_fullcurve@2019 Q1', 32: 'IR_Up25_fullcurve@2019 Q1', 33: 'IR_Up50@2019 Q1', 34: 'IR_Up75_fullcurve@2019 Q1', 35: 'IR_Up100_fullcurve@2019 Q1', 36: 'IR_Down1_fullcurve@2019 Q1', 37: 'IR_Down10_fullcurve@2019 Q1', 38: 'IR_Down25_fullcurve@2019 Q1', 39: 'IR_Down50@2019 Q1', 40: 'IR_Down75_fullcurve@2019 Q1', 41: 'IR_Down100_fullcurve@2019 Q1'},
                    'EOF': {0: 12000.432899449515, 1: 13000.378585638829, 2: 14000.823430270368, 3: 14000.332401284057, 4: 14000.319948713253, 5: 14000.644204347645, 6: 14000.672153975063, 7: 14000.275643910321, 8: 14000.4114857288914, 9: 14000.549951547569, 10: 14000.711018883325, 11: 14000.87999860886, 12: 14000.354474451909, 13: 14000.314690002719, 14: 14000.220141896281, 15: 14000.859491104784, 16: 14000.411871229149, 17: 14000.387516780731, 18: 14000.563587065257, 19: 14000.728226547561, 20: 14000.359626625061, 21: 14000.432899449515, 22: 14000.378585638829, 23: 14000.823430270368, 24: 14000.332401284057, 25: 14000.319948713253, 26: 14000.644204347645, 27: 14000.672153975063, 28: 14000.275643910321, 29: 14000.4114857288914, 30: 14000.549951547569, 31: 14000.711018883325, 32: 14000.87999860886, 33: 14000.354474451909, 34: 14000.314690002719, 35: 14000.220141896281, 36: 14000.859491104784, 37: 14000.411871229149, 38: 14000.387516780731, 39: 14000.563587065257, 40: 14000.728226547561, 41: 14000.359626625061}, 
                    'SCR': {0: 6500.579427358105, 1: 6500.4459556556058, 2: 6500.559593825823, 3: 6500.8612456170276, 4: 6500.8822454406309, 5: 6500.4532995609306, 6: 6500.6268037881136, 7: 6500.5266874616182, 8: 6500.1189164091002, 9: 6500.4247209208115, 10: 6500.8749271187471, 11: 6500.1240418481348, 12: 6500.0138437103269, 13: 6500.1694669961253, 14: 6500.132433900927, 15: 6500.4768171395381, 16: 6500.2482053481526, 17: 6500.6190116772541, 18: 6500.1458193823064, 19: 6500.5158277942755, 20: 6500.4183814338885, 21: 6500.579427358105, 22: 6500.4459556556058, 23: 6500.559593825823, 24: 6500.8612456170276, 25: 6500.8822454406309, 26: 6500.4532995609306, 27: 6500.6268037881136, 28: 6500.5266874616182, 29: 6500.1189164091002, 30: 6500.4247209208115, 31: 6500.8749271187471, 32: 6500.1240418481348, 33: 6500.0138437103269, 34: 6500.1694669961253, 35: 6500.132433900927, 36: 6500.4768171395381, 37: 6500.2482053481526, 38: 6500.6190116772541, 39: 6500.1458193823064, 40: 6500.5158277942755, 41: 6500.4183814338885},
                    'SII-ratio': {0: 2.0, 1: 2.0, 2: 1.0, 3: 1.0, 4: 2.0, 5: 1.0, 6: 2.0, 7: 1.0, 8: 1.0, 9: 2.0, 10: 2.0, 11: 2.0, 12: 2.0, 13: 2.0, 14: 2.0, 15: 2.0, 16: 2.0, 17: 2.0, 18: 2.0, 19: 2.0, 20: 2.0, 21: 2.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 2.0, 26: 1.0, 27: 2.0, 28: 1.0, 29: 1.0, 30: 2.0, 31: 2.0, 32: 2.0, 33: 2.0, 34: 2.0, 35: 2.0, 36: 2.0, 37: 2.0, 38: 2.0, 39: 2.0, 40: 2.0, 41: 2.0}, 
                    'OF Expl.': {0: float('nan'), 1: 'Own Funds decrease due to lower market value of equities', 2: 'Own Funds decrease due to lower market value of real estate', 3: 'Own Funds decrease due to lower market value of mortgages', 4: 'Own Funds decrease due to lower market value of corporate bonds', 5: 'Own Funds decrease due to lower market value of sovereign bonds', 6: 'Own Funds decrease due to high valuation of Liabilities', 7: 'Own Funds decrease due to high valuation of Liabilities', 8: 'Own Funds decrease due to high valuation of Liabilities', 9: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 10: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 11: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 12: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 13: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 14: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 15: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 16: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 17: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 18: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 19: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 20: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 21: float('nan'), 22: 'Own Funds decrease due to lower market value of equities', 23: 'Own Funds decrease due to lower market value of real estate', 24: 'Own Funds decrease due to lower market value of mortgages', 25: 'Own Funds decrease due to lower market value of corporate bonds', 26: 'Own Funds decrease due to lower market value of sovereign bonds', 27: 'Own Funds decrease due to high valuation of Liabilities', 28: 'Own Funds decrease due to high valuation of Liabilities', 29: 'Own Funds decrease due to high valuation of Liabilities', 30: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 31: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 32: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 33: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 34: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 35: 'Own Funds decrease due to lower valuation of assets and liabiliets. ', 36: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 37: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 38: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 39: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 40: 'Own Funds decrease due to lower valuation of assets and liabilities. ', 41: 'Own Funds decrease due to lower valuation of assets and liabilities. '},
                    'SCR Expl.': {0: float('nan'), 1: 'SCR decreases as less capital is required due to decreased equity exposure ', 2: 'SCR decreases as less capital is required due to decreased real estate exposure ', 3: 'SCR decreases due to decreased exposure to mortgages', 4: 'SCR decreases due to decreased exposure to corporate bonds', 5: 'SCR decreases due to decreased exposure to sovereign bonds', 6: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 7: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 8: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 9: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 10: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 11: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 12: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 13: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 14: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 15: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 16: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 17: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 18: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 19: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 20: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 21: float('nan'), 22: 'SCR decreases as less capital is required due to decreased equity exposure ', 23: 'SCR decreases as less capital is required due to decreased real estate exposure ', 24: 'SCR decreases due to decreased exposure to mortgages', 25: 'SCR decreases due to decreased exposure to corporate bonds', 26: 'SCR decreases due to decreased exposure to sovereign bonds', 27: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 28: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 29: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 30: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 31: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 32: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 33: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 34: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 35: 'SCR decreases mainly due to lower Interest Rate Risk and lower Mortality Risk', 36: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 37: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 38: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 39: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 40: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk', 41: 'SCR increases mainly due to higher Interest Rate Risk and higher Mortality Risk'}} ) 

@app.route('/')
def test():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    #df = pd.read_excel(w_dir + 'example7.xlsx')
    dash_app1 = dash.Dash(__name__, server = app, external_stylesheets = external_stylesheets, url_base_pathname='/')
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
                    value = 200,
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

#@app.route('/')
#def render_dashboard():
#    return flask.redirect('/dashboard/')

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
