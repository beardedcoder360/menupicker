from flask_app.config.mysqlconnection import connectToMySQL
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Customer:
    db_name = 'menupicker'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO customers (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM customers;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM customers WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM customers WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_customer(customer):
        is_valid = True
        query = "SELECT * FROM customers WHERE email = %(email)s;"
        results = connectToMySQL(Customer.db_name).query_db(query,customer)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(customer['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(customer['first_name']) < 2:
            flash("OH SNAP first name must be atleast 2 char","register")
            is_valid= False
        if len(customer['last_name']) < 2:
            flash("OH SNAP last name must be atleast 2 char","register")
            is_valid= False
        if len(customer['password']) < 8:
            flash("OH SNAP password must be atleast 8 char","register")
            is_valid= False
        if customer['password'] != customer['confirm']:
            flash("Somethings fishy passwords dont match","register")
        return is_valid