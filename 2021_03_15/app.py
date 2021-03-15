from flask import Flask
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
    Retrieve the menu of the town and return it.
    '''
    return 'This method should return json of the town menu.'

@app.route('/geojson/town/<towncode>/', methods = ['GET'])
def gj_town(towncode):
    '''
    Your code here.
    Retrieve the geojson of the town and return it.
    '''
    return 'This method should return the geojson of the town.'


if __name__ == "__main__":
    '''
    Your code here.
    Prepare data for the town() method.
    '''
    app.run(debug=True)