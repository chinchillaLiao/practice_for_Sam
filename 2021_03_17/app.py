from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/echo/<input>/', methods = ['GET'])
def echo(input):
    return f'{input}'
    
@app.route('/menu/town/', methods = ['GET'])
def menu_town():
    '''
    Your code here.
    Retrieve the menu of the town from database and return it.
    '''
    return 'This method should return json of the town menu.'

@app.route('/feature/town/<towncode>/', methods = ['GET'])
def gj_town(towncode):
    conn = sqlite3.connect('practica.db')
    (feature,) = conn.execute('select feature from town_features where towncode = ?' , (towncode, ) ).fetchone()
    conn.close()
    
    return feature


if __name__ == "__main__":
    app.run(debug=True)