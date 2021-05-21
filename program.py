from flask import Flask, render_template, url_for, request, redirect,flash,session
from dbcon import PostgresManagement

app = Flask(__name__)
app.secret_key = 'grimmteshco'
postgres = PostgresManagement()

@app.route('/')
def index():
    patient = postgres.findPatients()
    count = postgres.findCountAll()
    return render_template('index.html', patient=patient,count=count)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/people')
def people():
    person = postgres.findUsers()
    return render_template('pages/people.html', person=person)

@app.route('/patients')
def patients():
    patient = postgres.findPatients()
    return render_template('pages/patients.html', patient=patient)

@app.route('/doctors')
def doctors():
    person = postgres.findDoctors()
    return render_template('pages/doctors.html', person=person)

@app.route('/nurses')
def nurse():
    person = postgres.findNurse()
    return render_template('pages/nurse.html', person=person)

@app.route('/pharmacy')
def pharmacies():
    pharmacy = postgres.findPharmacy()
    return render_template('pages/pharmacy.html', pharmacy=pharmacy)


if __name__ == '__main__':
    app.run(debug=True)