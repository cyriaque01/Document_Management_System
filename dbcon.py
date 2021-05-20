import psycopg2
import sys, os
import numpy as np
import pandas as pd
from werkzeug.utils import find_modules
import credential__sql as creds
import pandas.io.sql as psql

## ****** LOAD PSQL DATABASE ***** ##

'''
# Set up a connection to the postgres server.
conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
+" password="+ creds.PGPASSWORD
conn=psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()


def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print (sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return (data)


#data = load_data('public','person')
#print(data)
'''
class PostgresManagement:
    def __init__(self):
        # Set up a connection to the postgres server.
        conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
            +" password="+ creds.PGPASSWORD
        conn=psycopg2.connect(conn_string)
        self.connection = conn
        #self.cursor = conn.cursor()
        self.schema = 'public'
    
    def findUsers(self):
        sql_command = "SELECT * FROM public.{};".format('person')
        #print (sql_command)
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    
    def findPatients(self):
        sql_command = "SELECT * FROM public.{};".format('patient')
        #print (sql_command)
        data = pd.read_sql(sql_command, self.connection)
        return (data) 


if __name__ == "__main__":
    postgresDB = PostgresManagement()
    res = postgresDB.findPatients()
    print(res)