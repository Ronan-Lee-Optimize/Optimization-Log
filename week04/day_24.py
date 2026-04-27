# day 24 - review: lists and dictionaries combined
# opt-log | consistency over perfection.

subjects = ["math", "english", "korean"]  # list

scores = {}                                # empty dictionary



for subj in subjects:
    
    score = int(input(f"Score for {subj}: "))
    
    scores[subj] = score                  # add to dictionary



print()

for subj, score in scores.items():
    
    if score >= 90:
        print(f"{subj}: {score} - lit 🔥")
        
    elif score >= 70:
        print(f"{subj}: {score} - good 👊")
        
    else:
        print(f"{subj}: {score} - mid 😪")


# 24K MAGIC THROUGH THE AIRRRRRRRRR
