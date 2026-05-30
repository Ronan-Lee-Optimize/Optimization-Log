# day 56 - build my own thing: GPA tracker
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.days = 0
        self.gpa = 0.0
        self.log = []



    def study(self, subject):
        self.days += 1
        self.log.append(subject)
        print(f"day {self.days}, {self.name} studied {subject}")



    def add_gpa(self, gpa):
        self.gpa = gpa
        
        if self.gpa >= 3.8:
            print(f"gpa: {self.gpa} - UC transfer is ready 🔥")
            
        elif self.gpa >= 3.5:
            print(f"gpa: {self.gpa} - getting there")
            
        else:
            print(f"gpa: {self.gpa} - push harder")



    def __str__(self):
        return f"{self.name} | target: {self.target} | days: {self.days} | gpa: {self.gpa}"



ronan = stu("ronan", "UCLA")
ronan.study("python")
ronan.study("math")
ronan.add_gpa(3.9)
print(ronan)
