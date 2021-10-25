from .shared import db

class Dataset(db.Model):
  dataset_datetime=db.Column(db.DateTime, primary_key=True)