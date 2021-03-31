from flask import Flask, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = (  '<div>Hello, World!</div>'
            + '<br>'
            + '<div>For map service, please visit:</div>'
            + '<div>http://127.0.0.1:5000/map</div>'
           )
    return text
    

@app.route('/map')
def map():
    '''
    The main page to show the map
    '''
    return render_template('map.html')

@app.route('/menu/town')
def menu_town():
    conn = sqlite3.connect('practica.db')
    (feature,) = conn.execute("select json from menus where name = 'town'"  ).fetchone()
    conn.close()
    
    return feature    

    


@app.route('/feature/town/<towncode>/', methods = ['GET'])
def gj_town(towncode):
    conn = sqlite3.connect('practica.db')
    (feature,) = conn.execute('select feature from town_features where towncode = ?' , (towncode, ) ).fetchone()
    conn.close()
    
    return feature    
    
@app.route('/favicon.ico')
def favicon():
    '''
    To draw a favicon, you can use free service like this:
    https://www.favicon.cc/?
    
    You can read more about adding a favicon in your flask app here:
    https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
    '''
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)