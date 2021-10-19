from .shared import db

class Enrollment(db.Model):
  course_id=db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True,)
  student_id=db.Column(db.Integer,db.ForeignKey('student.student_id'), primary_key=True)
  section=db.Column(db.String(10),primary_key=True)
  grade=db.Column(db.String(5))