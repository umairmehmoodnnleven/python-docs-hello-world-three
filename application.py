#from flask import Flask
import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World How are you doing? Test 1 2 3!"

@app.route('/test/')
def test():
    return "This is a test"

#from dash import Dash
#from werkzeug.wsgi import DispatcherMiddleware
#import flask
#from werkzeug.serving import run_simple
#import dash_html_components as html

#server = flask.Flask(__name__)
dash_app1 = Dash(__name__, server = app, url_base_pathname='/dashboard/' )
#dash_app2 = Dash(__name__, server = server, url_base_pathname='/reports/')
dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
#dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])
#@server.route('/')
#@server.route('/hello/')
#def hello():
#    return 'hello world!'

@app.route('/dash1/')
def render_dashboard():
    return flask.redirect('/dashboard/')


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
