import keyboard
from pyzbar import pyzbar

class Student: 
    attendedMeetings = {}

    def __init__(self, firstName, lastName, studentID, email):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        
