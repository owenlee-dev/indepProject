from .shared import db

class Student(db.Model):
  student_id=db.Column(db.Integer, primary_key=True)
  dataset=db.Column(db.DateTime,primary_key=True)
  name=db.Column(db.String(50),nullable=False)