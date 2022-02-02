from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/")
@app.route("/gallery")
def gallery_page():
    return render_template('gallery.html')


@app.route("/")
@app.route("/ElevationPlotTool")
def elevation_page():
    return render_template('elevation.html')


@app.route("/")
@app.route("/SummitDatabase")
def database_page():
    return render_template('database.html')