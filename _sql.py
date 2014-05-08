import pyodbc
import json
import collections
import gviz_api
import sys

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=WIN-2N5E8Q63188;DATABASE=LogMe;UID=LogMe;PWD=password')
cursor = cnxn.cursor()
cursor.execute("""
               SELECT RecordIndex, CounterValue
               FROM dbo.CounterData
               WHERE CounterDateTime BETWEEN ? AND ?
   AND CounterId = ?
               """, ['2014-05-03 21:19:03.156', '2014-05-03 21:21:18.146', 1])
rows = cursor.fetchall()
#rowarray_list = []
#for row in rows:
#    t = (row.RecordIndex, row.CounterValue)
#    rowarray_list.append(t)

# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['RecordIndex'] = row.RecordIndex
    d['CounterValue'] = row.CounterValue
    objects_list.append(d)

description ={"RecordIndex": ("number", "RecordIndex"),"CounterValue":("number", "CounterValue")}
data = objects_list


data_table = gviz_api.DataTable(description)
data_table.LoadData(data)
print
sys.stdout = open('file', 'w')
print data_table.ToJSonResponse(columns_order=("RecordIndex", "CounterValue"))
print data_table.ToJSon(columns_order=("RecordIndex", "CounterValue"))