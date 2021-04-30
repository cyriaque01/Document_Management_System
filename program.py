from flask import Flask, render_template, url_for, request, redirect,flash,session
from dbcon import PostgresManagement

app = Flask(__name__)
app.secret_key = 'grimmteshco'
postgres = PostgresManagement()

@app.route('/')
def index():
    user = postgres.findUsers()
    user = user.loc[0,'name':'surname']
    return render_template('index.html', name=user)


if __name__ == '__main__':
    app.run(debug=True)