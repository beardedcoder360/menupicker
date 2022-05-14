from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Answer:
    db_name = 'menupicker'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name =db_data['name']
        self.answer1 = db_data['answer1']
        self.answer2 = db_data['answer2']
        self.answer3 = db_data['answer3']
        self.answer4 = db_data['answer4']
        self.answer5 = db_data['answer5']
        self.customer_id = db_data['customer_id']


@classmethod
def save(cls,data):
    query = "INSERT INTO answers (answer1, answer2, answer3, answer4, answer5, customer_id) VALUES (%(answer1)s,%(answer2)s,%(answer3)s,%(answer4)s,%(answer5)s,%(customer_id)s);"
    return connectToMySQL(cls.db_name).query_db(query, data)


@staticmethod
def validate_answer(answer):
        if answer['answer1'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","answer")
        is_valid = True
        if answer['answer2'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","answer")
        is_valid = True
        if answer['answer3'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","answer")
        is_valid = True
        if answer['answer4'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","answer")
        is_valid = True
        if answer['answer5'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","answer")