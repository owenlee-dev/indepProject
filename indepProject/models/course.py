from .shared import db

class Course(db.Model):
  course_id=db.Column(db.Integer,primary_key=True)
  section=db.Column(db.String(10),primary_key=True)
  title=db.Column(db.String(50),primary_key=False)
  credit_hours=db.Column(db.Float,primary_key=False, nullable=False)
  dataset=db.Column(db.DateTime,db.ForeignKey('dataset.dataset_datetime'),primary_key=True)

  def __init__(self, course_id, section,dataset):
    self.course_id=course_id
    self.section=section
    self.dataset=dataset