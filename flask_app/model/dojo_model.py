from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model import ninja_model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Dojo:
    DB = 'Dojo_db'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []



    # SHOW ONE DOJO
    # =============================================================================================
    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM dojos  
        JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;"""
        
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojos_one = cls(results[0]) 
        print(results)

        for row_from_db in results:#Create an instance of collection
            ninjas_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['ninjas.first_name'],
                'last_name' : row_from_db['ninjas.last_name'],
                'age' : row_from_db['ninjas.age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at'],
                'dojo_id' : row_from_db['ninjas.dojo_id']
            }
            dojos_one.all_ninjas.append( ninja_model.Ninja(ninjas_data))
        return (dojos_one)
    


    # GET ALL DOJOS
    # =============================================================================================
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_dojo = []
        for dojo in results:
            all_dojo.append(cls(dojo))
        return all_dojo
    

    # CREATE DOJO
    # =============================================================================================
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos (name)
        VALUES (%(name)s);"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    

    


    # ADD DOJO
    # =============================================================================================
    @classmethod
    def add_dojo(cls, data):
        query = """INSERT INTO dojos (name)
        VALUES (%(name)s);"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

