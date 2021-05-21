from dbcon import PostgresManagement
class Functions:
    def __init__(self):
        table = ''
    
    def totalIncome(self,transactions):
        postgresDB = PostgresManagement()
        t,w,m,y = postgresDB.findSpecDate()
        
