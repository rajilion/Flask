'''
Created on Mar 23, 2019

@author: Rajkumar
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password@localhost:3306/test'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    dep = db.relationship('Department', backref='student_dept', lazy='dynamic')
    
class Department(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    
if __name__ == '__main__':
    manager.run()
                           

                           
    
    