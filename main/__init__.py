from flask import Flask,Blueprint
app=Flask(__name__)

from main.view.encrypt1 import enc

#BLUEPRINT REGISTER
app.register_blueprint(enc,url_prefix='/auth')
