from flask import Flask, render_template, url_for, request, redirect,flash,session
from dbcon import PostgresManagement

app = Flask(__name__)
app.secret_key = 'grimmteshco'
postgres = PostgresManagement()

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/people')
def people():
    person = postgres.findUsers()
    return render_template('pages/people.html', person=person)

@app.route('/patients')
def people():
    patient = postgres.findUsers()
    return render_template('pages/patients.html', patient=patient)


if __name__ == '__main__':
    app.run(debug=True)