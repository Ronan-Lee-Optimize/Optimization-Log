# day 32 - file read/write applied
# opt-log | consistency over perfection.

print("welcome to study log program.")



# write study log to file
with open("study_log.txt", "w") as f:
    subjects = ["math", "english", "korean"]

    
    for subj in subjects:
        hrs = int(input(f"hrs studied for {subj}: "))
        f.write(f"{subj}: {hrs} hrs\n")  # write each line



# read and print the log
with open("study_log.txt", "r") as f:
    print()
    print()
    print("---study log---")
    print(f.read())

# I WANT YOU BACK
