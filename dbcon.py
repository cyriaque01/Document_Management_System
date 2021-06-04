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
        sql_command = "SELECT * FROM person;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    def findUser(self, person):
        sql_command = "SELECT * FROM person WHERE id_person = {};".format(person)
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    
    def findPatients(self):
        sql_command = "SELECT *, patient.id_person as pa FROM patient INNER JOIN person on patient.id_person = person.id_person;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    
    def findDoctors(self):
        sql_command = "select *, doctor.id_person as pa from doctor inner join person on doctor.id_person = person.id_person;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    
    def findNurse(self):
        sql_command = "select *, nurse.id_person as pa from nurse inner join person on nurse.id_person = person.id_person;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)

    def findPharmacy(self):
        sql_command = "select * from pharmacy;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    def findCountAll(self):
        sql_command = "SELECT (SELECT COUNT(id_person) FROM person) AS person,(SELECT COUNT(id_doctor) FROM doctor) AS doctor,(SELECT COUNT(id_nurse) FROM nurse) AS nurse,(SELECT COUNT(id_product) FROM pharmacy) AS pharmacy, (SELECT COUNT(id_patient)FROM patient) AS patient;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)

    def findCashier(self):
        sql_command = "select *, cashier.id_person as ca from cashier inner join person on cashier.id_person = person.id_person;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    
    def findTransactions(self):
        sql_command = "select c.id_product,c.id_cashier,c.id_person,amount,date,p.name,p.surname, ph.name as product,ph.price from cashregister as c inner join person as p on c.id_person = p.id_person inner join pharmacy as ph on c.id_product = ph.id_product;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    def findAllTransactions(self):
        sql_command = "select * from cashregister;"
        data = pd.read_sql(sql_command, self.connection)
        return (data)
    def findSpecDate(self):
        sql_command = "select sum(total) as total from cashregister where date < (current_timestamp) and date > (current_timestamp -interval '1 day') "
        today = pd.read_sql(sql_command, self.connection)
        sql_command = "select sum(total) as total from cashregister where date < (current_timestamp) and date > (current_timestamp -interval '1 week') "
        week = pd.read_sql(sql_command, self.connection)
        sql_command = "select sum(total) as total from cashregister where date < (current_timestamp) and date > (current_timestamp -interval '1 month') "
        month = pd.read_sql(sql_command, self.connection)
        sql_command = "select sum(total) as total from cashregister where date < (current_timestamp) and date > (current_timestamp -interval '1 year') "
        year = pd.read_sql(sql_command, self.connection)
        return (today,week,month,year)


if __name__ == "__main__":
    postgresDB = PostgresManagement()
    t,w,m,y = postgresDB.findSpecDate()
    #person = postgresDB.findUsers()
    print(y.total)