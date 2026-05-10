# day 37 - review: try/except (applied)
# opt-log | consistency over perfection.

while True:
    try:
        num = int(input("enter a number (0 to quit): "))
        if num == 0:
            print("program stopped")
            break
        
        print(f"result: {100 / num}")


        
    except ValueError:
        print("not a number")
