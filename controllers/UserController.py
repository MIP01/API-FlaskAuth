from flask import jsonify, request
from config import get_db

def list():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT user_id, nama, nis, password, role FROM tbl_user"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return jsonify(result)

def show(user_id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT user_id, nama, nis, password, role FROM tbl_user WHERE user_id = ?"
    cursor.execute(query, [user_id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return jsonify(result)

def insert():
        db = get_db()
        cursor = db.cursor()
        details = request.json
        nama = details['nama']
        nis = details['nis']
        password = details['password']
        role = details['role']
        query = "INSERT INTO tbl_user(nama, nis, password, role) VALUES (?,?,?,?)"
        cursor.execute(query, [nama, nis, password, role])
        db.commit()
        return ('data inserted')

def update(user_id):
        db = get_db()
        cursor = db.cursor()
        details = request.json
        user_id = details['user_id']
        nama = details['nama']
        nis = details['nis']
        password = details['password']
        role = details['role']
        query = "UPDATE tbl_user SET nama = ?, nis = ?, password = ?, role = ? WHERE user_id = ?"
        cursor.execute(query, [nama, nis, password, role, user_id])
        db.commit()
        return ("data updated")

def delete(user_id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_user WHERE user_id = ?"
    cursor.execute(query, [user_id])
    db.commit()
    return ("data deleted")
