from credential__sql import PGPASSWORD
from flask.globals import request
from dbcon import PostgresManagement

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


"""
def newPerson(self,request):
        p = dict();
        p['name'] = request.form['fname']+' '+request.form['lname']
        p['type'] = request.form['type']
        p['phone'] = request.form['phone']
        p['pobox'] = request.form['pobox']
        p['addresse'] = request.form['adresse']
        p['email'] = request.form['email']

        return p

    def addNewPerson(self,request):
        person = self.newPerson(request)
        postgres.addPerson(person)
    """