class Classroom:
    def __init__(self, roomNumber, floor):
        self.roomNumber = roomNumber
        self.floor = floor

class School:
    def __init__ (self):
        self.classrooms = [Classroom(211, "1st"), Classroom(221, "2nd")]
