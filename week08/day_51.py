# day 51 - review: methods (applied)
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, days):
        self.name = name
        self.days = days



    def study(self, subject):
        self.days += 1
        print(f"{self.name} studied {subject}, and he studied for {self.days}days")



    def status(self):
        if self.days >= 50:
            print(f"{self.name}: locked in")
        else:
            print(f"{self.name}: keep going")



ronan = stu("ronan", 50)
ronan.study("python")
ronan.status()
