from flask import Flask, jsonify, request
from config import create_table
from routes.user_bp import user_bp
from routes.auth_bp import auth_bp

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.from_object('config')

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    return ('homepage')

@app.errorhandler(400)
def bad_req(error=None):
    message = {
        
            'status': 400,
            'message': 'Bad Request: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 400
    
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp

if __name__ == '__main__':
    create_table()
    app.debug = True
    app.run()