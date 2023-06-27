from flask_app.config.mysqlconnection import connectToMySQL
import re


class Ninja:
    DB = 'dojo_DB'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']



    # CREATE FROM SQL
    # =============================================================================================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        data = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in data:
            ninjas.append(cls(ninja))
        print(ninjas)
        return ninjas
    

    # SHOW ONE NINJA
    # =============================================================================================
    @classmethod
    def show_one(cls, data):
        query = """SELECT * FROM ninjas WHERE id = %(id)s;"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])



    # READ FROM SQL
    # =============================================================================================
    @classmethod
    def add_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    


    # choose dojo
    @classmethod
    def choose_dojo(cls, data):
        query = """SELECT * FROM ninjas WHERE dojo_id = %(id)s;"""
        
        results = connectToMySQL(cls.DB).query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    # UPDATE FROM SQL
    # @classmethod
    # def update(cls, data):
    #     query = """UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, dojo_id = %(dojo_id)s
    #     WHERE id = %(id)s;"""
    #     return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
    

    #  DELETE FROM SQL
    # @classmethod
    # def delete(cls, data):
    #     query = """DELETE FROM ninjas WHERE id = %(id)s;"""

    #     return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
