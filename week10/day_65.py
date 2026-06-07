# day 65 - review: random module (Applied)
# opt-log | consistency over perfection.

import random

subjects = ["math", "english", "korean", "science", "history"]

print("today's study schedule:")
random.shuffle(subjects)  # shuffle the list

for i, subj in enumerate(subjects):
    print(f"{i+1}. {subj}")
