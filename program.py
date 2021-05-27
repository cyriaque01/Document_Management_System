from flask import Flask, render_template, url_for, request, redirect,flash,session
from dbcon import PostgresManagement
from src.forms import VariousForms

app = Flask(__name__)
app.secret_key = 'grimmteshco'
postgres = PostgresManagement()
forms = VariousForms()

@app.route('/')
def index():
    patient = postgres.findPatients()
    count = postgres.findCountAll()
    t,w,m,y = postgres.findSpecDate()
    return render_template('index.html', patient=patient,count=count,t=t,w=w,m=m,y=y)

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

@app.route('/cashier')
def cashier():
    person = postgres.findCashier()
    return render_template('pages/cashier.html', person=person)

@app.route('/transactions')
def transactions():
    transaction = postgres.findTransactions()
    return render_template('pages/transactions.html', transaction=transaction)

@app.route('/new_person', methods=['GET','POST'])
def new_person():
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewPerson(request)
        return redirect(url_for('people'))
    return render_template('forms/new_person.html')


@app.route('/new_doctor', methods=['GET','POST'])
def new_doctor():
    person = postgres.findUsers()
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewDoctor(request)
        return redirect(url_for('doctors'))
    return render_template('forms/new_doctor.html', person=person)

@app.route('/new_nurse', methods=['GET','POST'])
def new_nurse():
    person = postgres.findUsers()
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewNurse(request)
        return redirect(url_for('nurse'))
    return render_template('forms/new_nurse.html', person=person)

@app.route('/new_cashier', methods=['GET','POST'])
def new_cashier():
    person = postgres.findUsers()
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewCashier(request)
        return redirect(url_for('cashier'))
    return render_template('forms/new_cashier.html', person=person)

@app.route('/new_patient', methods=['GET','POST'])
def new_patient():
    person = postgres.findUsers()
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewPatient(request)
        return redirect(url_for('patients'))
    return render_template('forms/new_patient.html', person=person)

@app.route('/new_pharmacy', methods=['GET','POST'])
def new_pharmacy():
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewPharmacy(request)
        return redirect(url_for('pharmacy'))
    return render_template('forms/new_pharmacy.html')



@app.route('/new_transaction', methods=['GET','POST'])
def new_transaction():
    person = postgres.findUsers()
    cashier = postgres.findCashier()
    pharmacy = postgres.findPharmacy()
    if request.method == 'POST' and len(request.form) >0:
        forms.addNewTransaction(request)
        return redirect(url_for('transactions'))
    return render_template('forms/new_transaction.html', person=person, cashier=cashier, pharmacy=pharmacy)









@app.route('/testSelect')
def tesSelect():
    person = postgres.findUsers()
    return render_template('forms/new_doctor.html', person=person)



if __name__ == '__main__':
    app.run(debug=True)