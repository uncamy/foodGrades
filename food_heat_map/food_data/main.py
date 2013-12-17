import pandas as pd
import os

from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
#configuration
DEBUG = True
CSV = 'data/reduced_man_geocoded_zip.csv'
df = pd.read_csv(CSV)
app = Flask(__name__)
app.config.from_object(__name__)

data = df[['geocode', 'CURRENTGRADE']]

data_non_missing = data[pd.notnull(data['CURRENTGRADE'])]


@app.route('/', methods = ['GET', 'POST'])
def index():
        man_grades = data_non_missing.to_json()
        return render_template('index.html', man_grades = man_grades)

if __name__ == '__main__':
    app.run()
data_non_missing.to_json('man_grades.json')
