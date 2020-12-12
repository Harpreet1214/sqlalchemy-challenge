# Dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta
from flask import Flask,jsonify


engine = create engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect = True)
session = Session(engine)

# Define name of classes
Measurement = Base.classes.measurement
Station = Base.classes.station


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

@app.route("api/v1.0/precipitation")
def percipitation():
    maxDate = dt.datex(2017,8,23)
    yearago = maxDate - dt.timedelta(days=365)

    past_temp = (session.query(measurement.date, measurement.prcp)
            .filter(measurement.date<=maxDate)
            .filter(measurement.date>=yearago)
            .order_by(measurement.date).all())

            
            
