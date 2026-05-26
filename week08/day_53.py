# day 53 - review: __str__ (applied)
# opt-log | consistency over perfection.

class transfstu:
    def __init__(self, name, days, target):
        self.name = name
        self.days = days
        self.target = target


    def __str__(self):
        return f"{self.name} | target: {self.target} | days: {self.days}"



ronan = transfstu("ronan", 53, "GOD OF CODING")
print(ronan)
