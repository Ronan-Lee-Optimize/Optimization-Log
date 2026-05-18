# day 45 - class inheritance
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def int(self):
        print(f"i'm {self.name}, studied for {self.days} days.")

class transfstu(stu):         # inherits from stu
    def __init__(self, name, days, goal):
        super().__init__(name, days)    # call parent init
        self.goal = goal

    def int(self):
        print(f"i'm {self.name}. my goal is {self.goal}. i studied {self.days} days.")

ronan = transfstu("ronan", 45, "uc transfer")
ronan.int()
