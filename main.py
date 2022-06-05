from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table_news
import news_models
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()
app.config['JSON_SORT_KEYS'] = False

users = {
    "user": generate_password_hash("hello"),
    "admin": generate_password_hash("admin")
}


@auth.get_user_roles
def get_user_roles(user):
    return user
def get_user_roles(admin):
    return user

@auth.verify_password
def authenticate(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
        


@app.route('/news', methods=['GET'])
@auth.login_required(role=['admin','user'])
def get_news():
    user = auth.current_user()
    if user == "admin":
        result = news_models.get_news()
        
        data = {
                
                'status': 200,
                'data': result
            
            }
      
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    else:
        result = news_models.get_user()
        
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp


@app.route('/news/<news_id>', methods=['GET'])
@auth.login_required(role='admin')
def get_news_by_id(news_id):
    try:
        result = news_models.get_news_by_id(news_id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
    
@app.route('/news', methods=['POST'])
@auth.login_required(role='admin')
def insert_news():
    
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.insert_news(title, content, datetime, flag)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp

@app.route('/news/<news_id>', methods=['PUT'])
@auth.login_required(role='admin')
def update_news(news_id):
    
    news_details = request.json
    news_id = news_details['news_id']
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.update_news(news_id, title, content, datetime, flag)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/news/<news_id>', methods=['PATCH'])
@auth.login_required(role='admin')
def patch_news(news_id):
    
    news_details = request.json
    news_id = news_details['news_id']
    flag = news_details['flag']
    result = news_models.patch_news(news_id, flag)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/news/<news_id>', methods=['DELETE'])
@auth.login_required(role='admin')
def delete_news(news_id):
    result = news_models.delete_news(news_id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
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

@app.errorhandler(405)
def server(error=None):
    message = {
            'status': 405,
            'message' : 'Method Not Allowed: ' + request.url,
            }
    resp = jsonify(message)
    resp.status_code = 405
    
    return resp
    
@app.errorhandler(400)
def server(error=None):
    message = {
            'status': 400,
            'message' : 'Bad Request: ' + request.url,
            }
    resp = jsonify(message)
    resp.status_code = 400
    
    return resp

if __name__ == "__main__":
    #create_table_news()
    #print(get_data())
    app.run(debug=True)
