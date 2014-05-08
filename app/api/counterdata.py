from flask import Response
import pyodbc
import json
import collections

from . import api

@api.route('/counterdata/<counterid>/<startdatetime>/<enddatetime>/')
def get_chart_data(counterid, startdatetime, enddatetime):
    return "Hello world! Here's the data: CounterID: %s, Start Date Time: %s, End Date Time: %s" % (
        counterid,
        startdatetime,
        enddatetime
    )