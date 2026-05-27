# day 54 - review: classes full practice
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, days):
        self.name = name
        self.days = days


    def study(self, subject):
        self.days += 1
        print(f"{self.name} studied {subject}. total days: {self.days}")


    def __str__(self):
        return f"{self.name} | days: {self.days}"



class transfstu(stu):
    def __init__(self, name, days, target):
        super().__init__(name, days)
        self.target = target


    def __str__(self):
        return f"{self.name} | target: {self.target} | days: {self.days}"



ronan = transfstu("ronan", 54, "ucla")
ronan.study("python")
ronan.study("math")
print(ronan)
