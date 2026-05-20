# day 47 - classes: full practice
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, goal, days):
        self.name = name
        self.goal = goal
        self.days = days



    def __str__(self):
        return f"{self.name} | goal: {self.goal} | days: {self.days}"



    def study(self):
        self.days += 1
        print(f"{self.name} studied. total days: {self.days}")



class transfstu(stu):
    def __init__(self, name, goal, days, target):
        super().__init__(name, goal, days)
        self.target = target



    def __str__(self):
        return f"{self.name} | goal: {self.goal} | target: {self.target} | days: {self.days}"



ronan = transfstu("ronan", "UC Transfer", 46, "UC Berkeley")
print(ronan)
ronan.study()
print(ronan)
