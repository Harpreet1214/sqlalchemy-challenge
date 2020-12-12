# Dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta
from flask import Flask,jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect = True)

# Define name of classes
Measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)

# Initiate Flask
app = Flask(__name__)

@app.route("/")
def home():
    """List all api routes that are available"""
    return(
    f"AvailableRoutes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/<start><br/>"
    f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    maxDate = dt.datex(2017,8,23)
    yearago = maxDate - dt.timedelta(days=365)

    past_temp = (session.query(Measurement.date, Measurement.prcp)
            .filter(Measurement.date<=maxDate)
            .filter(Measurement.date>=yearago)
            .order_by(Measurement.date).all())

        precip = {date: prcp for date, prcp in past_temp}

        return jsonify (precip)

@app.route("/api/v1.0/stations")
def stations():
    stations_all = session.query(station.station).all()

    return jsonify(stations_all)

@app.route("/api/v1.0/tobs")
def tobs():
    maxDate = dt.date(2017,8,23)
    year_ago = maxDate - dt.timedelta(days=365)
    temps = (session.query(Measurement.tobs)
        .filter(Measurement.station == most_active_station)
        .filter(Measurement..date<=maxDate)
        .filter((Measurement.date>=yearago)
        .order_by(Measurement.tobs).all())
        
        return jsonify (temps)

@app.route("/api/v1.0/<start>")
def start(start= None):
    maxDate = dt.date(2017,8,23)
    tobs_only = (session.query(Measurement.tobs)
                .filter(Measurement.date.between(start, maxDate)).all())

    tobs_df = pd.DataFrame(tobs_only)

    tavg = tobs_df["tobs"].mean()
    tmax = tobs_df["tobs"].max()
    tmin = tobs_df["tobs"].min()

        return jsonify(tavg, tmax, tmin)           

    @app.route("/api/v1.0/<start>/<end>")
def stend(start = none, end = none):
    tobs_only = (session.query(Measurement.tobs)
                .filter(Measurement.date.between(start, end)).all())

                tobs_df = pd.DataFrame(tobs_only)

    tavg = tobs_df["tobs"].mean()
    tmax = tobs_df["tobs"].max()
    tmin = tobs_df["tobs"].min()

        return jsonify(tavg, tmax, tmin)  

    if __name__ == '__main__':
        app.run (debug=True)    