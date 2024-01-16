from flask import Flask
from flask import render_template
from datetime import datetime
from waitress import serve

app = Flask(__name__)


def get_current_date():
  return {'curr_year': str(datetime.now().year)}


app.context_processor(get_current_date)


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/about/")
def about():
  return render_template("about.html")


@app.route("/api/data")
def get_data():
  return app.send_static_file("data.json")


if __name__ == '__main__':
  serve(app, listen='*:80')
