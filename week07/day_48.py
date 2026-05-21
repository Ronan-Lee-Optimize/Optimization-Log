# day 48 - classes: mini project
# opt-log | consistency over perfection.



class stu:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.days = 0
        self.log = []  # study log list



    def study(self, subject):
        self.days += 1
        self.log.append(subject)  # add to log
        print(f"day {self.days}, {self.name} studied {subject}.")

    def __str__(self):
        return f"{self.name} | goal: {self.goal} | days: {self.days} | log: {self.log}"



ronan = stu("ronan", "uc transfer")
ronan.study("math")
ronan.study("python")
ronan.study("english")
print(ronan)
