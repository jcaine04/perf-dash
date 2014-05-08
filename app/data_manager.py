import pyodbc

from config import Config

class Database(object):

    def __init__(self):
        self.cnxn = None
        self.cur = None

    def connect(self):
        """Returns database connection"""
        try:
            self.cnxn = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
                Config.SQL_DRIVER,
                Config.SQL_SERVER,
                Config.SQL_DATABASE,
                Config.SQL_USER,
                Config.SQL_PASSWORD)
            )
        except:
            print "Unable to establish connection to database"
            exit(1)

    def get_cursor(self):
        """Returns a cursor for the database connection"""
        self.cur = self.cnxn.cursor()