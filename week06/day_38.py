# day 38 - review: file read/write (applied)
# opt-log | consistency over perfection.

name = input("enter your name: ")

days = int(input("days studied: "))

asp = input("enter your aspirations: ")



with open("study_log.txt", "w") as f:
    
    f.write(f"name: {name}\n")
    
    f.write(f"days studied: {days}\n")  # write to file
    
    f.write("keep going buddy\n")

    f.write(f"your aspirations: {asp}\n")



with open("study_log.txt", "r") as f:
    
    print()
    
    print("--- log ---")
    
    print(f.read())  # read from file


# the weather is getting hotter
