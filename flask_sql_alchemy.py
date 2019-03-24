'''
Created on Mar 23, 2019

@author: Rajkumar
'''

from flask_sqlalchemy import SQLAlchemy

from flask.app import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password@localhost:3306/test'
db = SQLAlchemy(app)

@app.route("/")
def test():
    student = Student('rajkumar.j', 'rajkumar.j@gmail.com')
    db.create_all() #create table
    db.session.add(student) #insert
    db.session.commit()
    results = Student.query.all() #fetch
    final_result = []
    for row in results:
        final_result.append('ID:{0}, Name:{1}, Email:{2}'.format(row.id, row.name, row.email))
    final_result = " ".join(final_result)
    return final_result


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return 'Name: {0}, Email: {1}'.format( self.name, self.email)


if __name__ == "__main__":
    app.run(debug=True)
