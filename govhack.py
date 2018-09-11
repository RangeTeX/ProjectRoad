import json

from flask import Flask, render_template
from scripts import trafficdata
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask import flash, redirect, request, url_for

app = Flask(__name__)
CONFIG_FILE = json.loads(open("./config.json").read())
app.config['GOOGLEMAPS_KEY'] = CONFIG_FILE["key"]

GoogleMaps(app)


@app.route('/')
def map_view():
    high = False
    med = False
    low = False
    crash = False

    if 'high' in request.args:
        high = request.args.get('high')
    if 'med' in request.args:
        med = request.args.get('med')
    if 'low' in request.args:
        low = request.args.get('low')
    if 'crash' in request.args:
        crash = request.args.get('crash')
    map = Map(
        identifier="view-side",
        # bunjil place

        lat=-38.01973,
        lng=145.3008,
        center_on_user_location=True,
        style='height:500px;width:auto;margin:0;flex-grow:1;',
        # markers is a list of tuples
        # if we write a func that returns [(lat,long),(lat,long),...]
        # we can plot that shit :D
        # markers=[(-38.01973, -145.3008)]
        markers=trafficdata.get_hotspots(low, med, high, crash)
    )

    return render_template("map.html", map=map)


@app.route('/stats/')
def stats():
    return render_template('stats.html', stat_hotspots=trafficdata.num_points(),
                           stat_highest=trafficdata.get_max_load())


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/git')
def gitlink():
    return redirect("https://github.com/rawrxdee/ProjectRoad")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
