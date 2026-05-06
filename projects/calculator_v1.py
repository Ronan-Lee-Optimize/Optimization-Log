print("Welcome to basic calculator!")
print()
print()


first = int(input("enter 1st number: "))
print()

print("choose arithmetic operators (1: (+), 2: (-), 3: (*), 4: (/))")
oper = int(input(": "))
print()

second = int(input("enter 2nd number: "))
print()
print("result: ")

if oper == 1:
    print(first+second)

elif oper == 2:
    print(first-second)

elif oper == 3:
    print(first*second)

elif oper == 4:
    print(first/second)
