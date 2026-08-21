# day 137 - id and score lookup tool (applied)
# opt-log | consistency over perfection.

scores = {}

while True:
    student_id = input("enter student id (or 'done' to stop): ")

    if student_id == "done":
        break
    score = int(input(f"enter score for {student_id}: "))
    scores[student_id] = score


print()
print("all entries recorded:")
print(scores)


print()
search_id = input("enter an id to look up: ")


if search_id in scores:
    print(f"{search_id}'s score: {scores[search_id]}")
    
else:
    print(f"{search_id} not found in records")
