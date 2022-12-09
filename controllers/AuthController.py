from flask import request, jsonify
from config import get_db

def validate_nis(nis):
    db = get_db()
    cursor = db.cursor()
    find_nis = ("SELECT * FROM tbl_user WHERE nis = ?")
    cursor.execute(find_nis,[(nis)])
    results = cursor.fetchall()             
    return results

def validate_role(nis, role):
    db = get_db()
    cursor = db.cursor()
    find_role = ("SELECT * FROM tbl_user WHERE nis = ? AND role = ?")
    cursor.execute(find_role, [(nis), (role)])
    result = cursor.fetchall()
    return result

def login():
        db = get_db()
        details = request.json
        nis = details['nis']
        role = details['role']

        if (validate_nis(nis)):
            if (validate_role(nis, role)):
                return jsonify('welcome',nis)
            else:
                return('wrong role')
        else:
            return("data no avaible")
        
       

def logout():
    pass