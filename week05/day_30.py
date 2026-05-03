# day 30 - try/except advanced
# opt-log | consistency over perfection.

try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = num1 / num2
    
    print(f"result: {result}")



except ValueError:
    print("not a number.")   # wrong input type

    
except ZeroDivisionError:
    print("can't divide by zero.") # division by zero
