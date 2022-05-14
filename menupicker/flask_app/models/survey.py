from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    db_name = 'menupicker'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name =db_data['name']
        self.option1 = db_data['option1']
        self.option2 = db_data['option2']
        self.option3 = db_data['option3']
        self.option4 = db_data['option4']
        self.option5 = db_data['option5']
        self.option6 = db_data['option6']
        self.option7 = db_data['option7']
        self.option8 = db_data['option8']
        self.option9 = db_data['option9']
        self.option10 = db_data['option10']
        self.user_id = db_data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO surveys (name,option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, user_id) VALUES (%(name)s,%(option1)s,%(option2)s,%(option3)s,%(option4)s,%(option5)s,%(option6)s,%(option7)s,%(option8)s,%(option9)s,%(option10)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM surveys WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM surveys;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_surveys = []
        for row in results:
            all_surveys.append( cls(row) )
        return all_surveys

    @classmethod
    def update(cls, data):
        query = "UPDATE surveys SET name = %(name)s,option1= %(option1)s, option2=%(option2)s, option3=%(option3)s, option4=%(option4)s,option5=%(option5)s,option6=%(option6)s,option7=%(option7)s,option8=%(option8)s,option9=%(option9)s,option10=%(option10)s,updated_at=NOW() where id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one(cls,data):
        query = "select * from surveys where id =%(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])


    @staticmethod
    def validate_survey(survey):
        if survey['name'] == "":
            is_valid = False
            flash("you have to have a name","survey")
        is_valid = True
        if survey['option1'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option2'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option3'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option4'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option5'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option6'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option7'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option8'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option9'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        is_valid = True
        if survey['option10'] == "":
            is_valid = False
            flash("dont be lazy put something in the field!","survey")
        return is_valid