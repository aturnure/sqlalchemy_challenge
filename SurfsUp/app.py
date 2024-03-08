# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine) *Used individually for each route

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Weather Analysis in Honolulu, Hawaii<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Replace start and end with dates in the format: yyyy-mm-dd"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    past_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    past_year_rain = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= past_year).all()
    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_data = []
    for date, prcp in past_year_rain:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precipitation_data.append(precip_dict)

    # Return the JSON representation of the dictionary
    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all of the stations 
    stations = session.query(Station.station, Station.name).all()
    session.close()

    # Return a JSON list of stations from the dataset
    station_list = []
    for station, name in stations:
        station_dict = {}
        station_dict['station'] = station
        station_dict['name'] = name
        station_list.append(station_dict)

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    past_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the dates and temperature observations of the most-active station for the previous year of data
    active_station = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= past_year).all()
    session.close()

    # Return a JSON list of temperature observations for the previous year
    active_list = []
    for date, tobs in active_station:
        active_dict = {}
        active_dict['date'] = date
        active_dict['tobs'] = tobs
        active_list.append(active_dict)
    
    return jsonify(active_list)


@app.route("/api/v1.0/<start>")
def start_date(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the min, max, and average temperatures calculated from the given start date to the end of the dataset 
    temp_stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >=start).all()
    session.close()

    # Return json list
    temp_list = []
    for min, max, avg in temp_stats:
        temp_dict = {}
        temp_dict['min'] = min
        temp_dict['max'] = max
        temp_dict['avg'] = avg
        temp_list.append(temp_dict)

    return jsonify(temp_list)


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the min, max, and average temperatures calculated from the given start date to the given end date
    start_end = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >=start).\
        filter(Measurement.date <= end).all()
    session.close()
    
    # Return json list
    start_end_list = []
    for min, max, avg in start_end:
        start_end_dict = {}
        start_end_dict['min'] = min
        start_end_dict['max'] = max
        start_end_dict['avg'] = avg
        start_end_list.append(start_end_dict)
    
    return jsonify(start_end_list)

if __name__ == '__main__':
    app.run(debug=True)
