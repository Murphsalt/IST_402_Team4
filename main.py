from flask import *
from flask_httpauth import HTTPBasicAuth
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth() #http authentication
currentTime = datetime.datetime.now() #current time on server
temp = [78.5,55.6] #Test numbers for temp
tasks = [
    {
        'RaspberryPi Number': 26,
        'Title': 'Temperature of RaspberryPi',
        'Temperature': temp[1],
        'Time:': currentTime
    },
    {
        'RaspberryPi Number': 20,
        'Title': 'Temperature of RaspberryPi',
        'Temperature': temp[0],
        'Time': currentTime
    }
]

@app.route('/', methods=['GET'])
@auth.login_required #get login information
def get_tasks():
    return jsonify({'tasks': tasks})

@app.errorhandler(404) #error handler
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@auth.get_password #creates user
def get_password(username):
    if username == 'pi':
        return 'team4pi'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
