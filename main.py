import pandas as pd
import os

from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
#configuration
DEBUG = True
CSV = './data/manhattan_grades.csv'
df = pd.read_csv(CSV)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
