from flask import Flask
from views import MainHandler, JSHandler, CSSHandler, FeatureHandler
from settings import app


app.add_url_rule('/static/js/<path:path>', view_func=JSHandler.as_view('js'))
app.add_url_rule('/static/css/<path:path>', view_func=CSSHandler.as_view('css'))
app.add_url_rule('/feature/create/', view_func=MainHandler.as_view('feature'))
app.add_url_rule('/features/', view_func=FeatureHandler.as_view('featurepage'))
app.add_url_rule('/feature/getall/', view_func=FeatureHandler.as_view('getallfeatures'))
app.add_url_rule('/', view_func=MainHandler.as_view('main'))
