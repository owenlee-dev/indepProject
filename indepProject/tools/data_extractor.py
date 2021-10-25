# import sys
# sys.path.append('../')
import csv
from ..models import Enrollment, Student, Course, db

# Function to extract data from an input file and save in a list of dictionaries
def Text_to_dictionary_list(input_file):
  subject_list=[]
  with open(input_file,'r', newline='') as subjects:
    subject_reader=csv.DictReader(subjects,delimiter="\t")
    for subject in subject_reader:
      subject_list.append(subject)
  return subject_list

# Function to insert a record into the student table

# Function to insert a record into the course table

# Function to insert a record into the enrollment table
def Insert_enrollment(id,s_id,sect,gr):
  record=Enrollment(course_id=id, student_id=s_id, section=sect, grade=gr)
  db.session.add(record)
  db.session.commit()


