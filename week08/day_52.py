# day 52 - review: inheritance (applied)
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, days):
        self.name = name
        self.days = days


    def study(self, subject):
        self.days += 1
        print(f"{self.name} studied {subject}. total days: {self.days}")



class transfstu(stu):
    def __init__(self, name, days, target):
        super().__init__(name, days)
        self.target = target


    def status(self):
        print(f"{self.name} is aiming for {self.target}. days: {self.days}")



ronan = transfstu("ronan", 51, "UCLA")
ronan.study("python")
ronan.status()
