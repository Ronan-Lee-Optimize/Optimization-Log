# day 43 - classes
# opt-log | consistency over perfection.

class stu:
    def __init__(self, name, days):
        self.name = name    # store name
        self.days = days    # store days



ronan = stu("ronan", 43)  # create an object


print(ronan.name)   # access attribute

print(ronan.days)



class stu:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def int(self):
        print(f"i'm {self.name}, studied for {self.days} days")  # method

ronan = stu("ronan", 43)
ronan.int()  # call the method
