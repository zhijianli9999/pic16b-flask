# to run this website and watch for changes:
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sklearn as sk
# import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)


@app.route('/')
def main():
    return render_template('main_better.html')


@app.route('/view/')
def view():
    return render_template('view.html')


@app.route('/submit/')
def submit():
    return render_template('submit.html')


# def get_message_db():
