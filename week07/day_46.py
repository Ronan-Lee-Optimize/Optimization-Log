# day 46 - classes: __str__ method
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, goal, days):
        self.name = name
        self.goal = goal
        self.days = days



    def __str__(self):
        return f"{self.name} | goal: {self.goal} | days: {self.days}"  # print-friendly



ronan = stu("ronan", "be a god of python", 46)
print(ronan)  # calls __str__ automatically

# ICEMAN
