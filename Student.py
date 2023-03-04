import keyboard
from pyzbar import pyzbar
import ast

class Student: 
    

    def __init__(self, studentID, lastName, firstName, email, attendedMeetings):
        self.studentID = studentID
        self.lastName = lastName
        self.firstName = firstName
        self.email = email
        self.attendedMeetings = ast.literal_eval(attendedMeetings)
        
