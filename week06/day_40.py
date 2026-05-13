# day 40 - review: lambda (applied)
# opt-log | consistency over perfection.

students = [
    {"name": "ronan", "score": 91},
    {"name": "jungmin", "score": 85}
]

students.sort(key=lambda x: x["score"], reverse=True)  # sort by score



for s in students:
    print(f"{s['name']}: {s['score']}")  # print ranked
