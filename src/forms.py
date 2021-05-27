from credential__sql import PGPASSWORD
from flask.globals import request
from dbcon import PostgresManagement
from datetime import datetime

postgres = PostgresManagement()

class VariousForms():
    def __init__(self) -> None:
        pass
    
    def newPerson(self,request):
        
        name = request.form['fname']
        surname = request.form['lname']
        type = request.form['type']
        phone = request.form['phone']
        pobox = request.form['pobox']
        addresse = request.form['adresse']
        email = request.form['email']

        return name,surname, type, phone, pobox, email, addresse

    def addNewPerson(self,request):
        postgres.addPerson(self.newPerson(request))

    def newDoctor(self,request):
        id_person = request.form['person']
        speciality = request.form['speciality']
        hoursstart = request.form['hoursstart']
        hoursend = request.form['hoursend']

        return id_person, speciality, hoursstart, hoursend

    def addNewDoctor(self,request):
        postgres.addDoctor(self.newDoctor(request))

    def newNurse(self,request):
        id_person = request.form['person']
        hoursstart = request.form['hoursstart']
        hoursend = request.form['hoursend']

        return id_person, hoursstart, hoursend

    def addNewNurse(self,request):
        postgres.addNurse(self.newNurse(request))

    
    def newCashier(self,request):
        id_person = request.form['person']
        password = request.form['password']
        hoursstart = request.form['hoursstart']
        hoursend = request.form['hoursend']

        return id_person, password, hoursstart, hoursend

    def addNewCashier(self,request):
        postgres.addCashier(self.newCashier(request))    

    def newPatient(self,request):
        id_person = request.form['person']
        date = request.form['checkin']
        room = request.form['roomnumber']
        checkout = request.form['checkout']
        diagnosis = request.form['diagnosis']

        return id_person, date, room, checkout,diagnosis

    def addNewPatient(self,request):
        postgres.addPatient(self.newPatient(request))    

    def newPharmacy(self,request):
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']

        return  name, price, stock

    def addNewPharmacy(self,request):
        postgres.addPharmacy(self.newPharmacy(request))  

    def newTransaction(self,request):
        id_cashier = request.form['cashier']
        id_product = request.form['product']
        id_person = request.form['person']
        amount = request.form['amount']
        date = datetime.now()
        date = date.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        total = postgres.getProductPrice(id_product)*float(amount) 
       

        return id_cashier, id_product, id_person, amount, date, total

    def addNewTransaction(self,request):
        postgres.addTransaction(self.newTransaction(request))  