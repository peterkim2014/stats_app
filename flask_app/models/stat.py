from flask_app.config.mysqlconnection import MySQLConnection

class Stat:
    def __init__(self, data):
        self.username = data["user_name"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



