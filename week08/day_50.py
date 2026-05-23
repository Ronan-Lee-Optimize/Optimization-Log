# day 50 - review: classes and __init__
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, goal, days):
        self.name = name
        self.goal = goal
        self.days = days



ronan = stu("ronan", "god of coding", 50)
print(ronan.name)
print(ronan.goal)
print(ronan.days)
