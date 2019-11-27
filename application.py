# from flask import Flask

from dash import Dash
from werkzeug.wsgi import DispatcherMiddleware
import flask
import dash_html_components as html

server = Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/dashboard/' )
dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])

@server.route('/')
@server.route("/hello/")
def hello():
    return "Hello World How are you doing? Test 1 2 3!"

@server.route('/dashboard/')
def render_dashboard():
    return flask.redirect('/dash1/')

app = DispatcherMiddleware(server, {
    '/dash1/': dash_app1.server})
