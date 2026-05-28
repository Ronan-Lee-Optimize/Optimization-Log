# day 55 - review: classes mini project (applied)
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.days = 0
        self.log = []


    def study(self, subject):
        self.days += 1
        self.log.append(subject)
        print(f"day {self.days}, {self.name} studied {subject}")


    def __str__(self):
        return f"{self.name} | target: {self.target} | days: {self.days} | log: {self.log}"



name = input("enter ur name: ")
target = input("enter ur target: ")

ronan = stu(name, target)



while True:
    subject = input("what did u study? (quit to stop): ")
    if subject == "quit":
        break
    ronan.study(subject)


print()
print(ronan)
