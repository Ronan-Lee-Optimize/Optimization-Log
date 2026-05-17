# day 44 - classes: adding methods
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, goal, days):
        self.name = name
        self.goal = goal
        self.days = days



    def int(self):
        print(f"i'm {self.name}. my goal is {self.goal}.")  # introduce



    def study(self):
        self.days += 1                                 # add a day
        print(f"total days {self.name} studied: {self.days}")



ronan = stu("ronan", "UC transfer", 43)
ronan.int()
ronan.study()
ronan.study()
