import pyodbc
import json
import collections

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=WIN8\MSSQL2K12;DATABASE=LogMe;UID=LogMe;PWD=password')
cursor = cnxn.cursor()
cursor.execute("""
               SELECT
               CounterID,
               MachineName,
               CONCAT(ObjectName, '' ,CounterName) AS 'CounterName',
               ISNULL(InstanceName, '') AS 'Instances'
               FROM dbo.CounterDetails
               """)
rows = cursor.fetchall()

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['CounterID'] = row.CounterID
    d['MachineName'] = row.MachineName
    d['CounterName'] = row.CounterName
    d['Instances'] = row.Instances
    objects_list.append(d)
j = json.dumps(objects_list)

print j
