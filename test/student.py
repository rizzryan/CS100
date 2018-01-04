class Student(object):
    """docstring for Student."""
    # PART A
    def __init__(self, stuName, stuID, gpa):
        self.stuName = stuName
        self.stuID = stuID
        self.gpa = gpa

    def displayInfo(self):
        print('Student name: ' + self.stuName + '\nStudent id: ' + self.stuID + '\nStudent gpa: ' + str(self.gpa))

    def gradWithHonors(self):
        if self.gpa >= 3.8:
            return True
        else:
            return False
