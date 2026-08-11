# day 129 - bridge week: id and score lookup tool (applied)
# opt-log | Consistency over perfection.

scores = {}

# collect id/score pairs from the user
while True:
    student_id = input("enter student id (or 'done' to stop): ")
    if student_id == "done":
        break
    score = int(input(f"enter score for {student_id}: "))
    scores[student_id] = score


print()
print("all entries recorded:")
print(scores)


# now let the user search by id
print()
search_id = input("enter an id to look up: ")


if search_id in scores:
    print(f"{search_id}'s score: {scores[search_id]}")
else:
    print(f"{search_id} not found in records")
