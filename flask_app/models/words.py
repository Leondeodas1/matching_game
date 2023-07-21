from flask_app.config.mysqlconnection import connectToMySQL
import random

mydb = 'the_match'

class random_word:
    something = " "
    def __init__(self,data):
        self.id = data["id"]
        self.theword = data["theword"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def word_generator(cls,data):
        query = "INSERT INTO random_word(theword,created_at, updated_at) VALUES (%(theword)s, NOW(), NOW())"
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def does_it_match(cls,data):
        list = []
        for val in data.values():
            list.append(val)
        findout = "".join(list)
        query = "Select * from random_word ORDER BY random_word.id desc"
        print(cls.something, findout)
        return connectToMySQL(mydb).query_db(query)
    
    @classmethod
    def hint(cls):
        query = "Select * from random_word ORDER BY random_word.id desc"
        
        results = connectToMySQL(mydb).query_db(query)
        matching = results[0]["theword"]
        cls.something = matching
        return results
