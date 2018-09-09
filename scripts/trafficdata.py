import os
import json

traffic_data = json.loads(open('traffic.json').read())
crash_data = json.loads(open('crash.json').read())


def get_hotspots(low, med, high, crash):
    markers = []
    for entry in traffic_data:
        if low:
            if entry["ALLVEHS_AADT"] <= 500:
                markers.append({
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': entry["MIDPNT_LAT"],
                    'lng': entry["MIDPNT_LON"],
                    'infobox': '<h3>Road name: %s</h3><p>Flow Direction: %s</p><p>Average Vehicles: %s</p><p>Average Trucks: %s</p>' % (
                        entry["HMGNS_LNK_DESC"], entry["FLOW"], entry["ALLVEHS_AADT"], entry["TRUCKS_AADT"])
                })
        if med:
            if entry["ALLVEHS_AADT"] > 500 & entry["ALLVEHS_AADT"] < 10000:
                markers.append({
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                    'lat': entry["MIDPNT_LAT"],
                    'lng': entry["MIDPNT_LON"],
                    'infobox': '<h3>Road name: %s</h3><p>Flow Direction: %s</p><p>Average Vehicles: %s</p><p>Average Trucks: %s</p>' % (
                        entry["HMGNS_LNK_DESC"], entry["FLOW"], entry["ALLVEHS_AADT"], entry["TRUCKS_AADT"])
                })
        if high:
            if entry["ALLVEHS_AADT"] >= 10000:
                markers.append({
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                    'lat': entry["MIDPNT_LAT"],
                    'lng': entry["MIDPNT_LON"],
                    'infobox': '<h3>Road name: %s</h3><p>Flow Direction: %s</p><p>Average Vehicles: %s</p><p>Average Trucks: %s</p>' % (
                        entry["HMGNS_LNK_DESC"], entry["FLOW"], entry["ALLVEHS_AADT"], entry["TRUCKS_AADT"])
                })
    markers.extend(get_crashes(crash))
    return markers


def get_crashes(crash):
    crashes = []
    if crash:
        for entry in crash_data:
            crashes.append({
                'icon': 'https://rangeent.com/carbingg.png',
                'lat': entry["LATITUDE"],
                'lng': entry["LONGITUDE"],
                'infobox': '<h3>Crash</h3><p>Accident Type: %s</p><p>Accident Severity: %s</p>' % (
                entry["ACCIDENT_TYPE"], entry["SEVERITY"])
            })
    return crashes


def get_max_load():
    load = 0
    for entry in traffic_data:
        if (entry["ALLVEHS_AADT"] > load):
            load = entry["ALLVEHS_AADT"]
    return load


def num_points():
    count = 0
    for entry in traffic_data:
        count += 1
    return count
