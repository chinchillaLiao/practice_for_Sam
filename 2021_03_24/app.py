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