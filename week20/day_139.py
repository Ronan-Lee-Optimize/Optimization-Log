# day 139 - review: simple grade manager (applied)
# opt-log | consistency over perfection.

def get_students():
    students = []
    while True:
        name = input("enter student name (or 'done' to stop): ")
        if name == "done":
            break
        score = int(input(f"enter {name}'s score: "))
        students.append({"name": name, "score": score})
    return students


def get_average(students):
    total = 0
    for s in students:
        total = total + s["score"]
    return total / len(students)


def get_top_students(students, cutoff):
    top = []
    for s in students:
        if s["score"] >= cutoff:
            top.append(s)
    return top


roster = get_students()


print()
print(f"class average: {get_average(roster):.1f}")


top_students = get_top_students(roster, 80)

print()
print("students with 80 or above:")
for s in top_students:
    print(f"{s['name']}: {s['score']}")
