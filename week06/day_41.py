# day 41 - review: *args (applied)
# opt-log | consistency over perfection.

def score_total(*args):
    print(f"scores: {args}")
    print(f"total: {sum(args)}")
    print(f"average: {sum(args) / len(args)}")  # calculate average



score_total(85, 90, 78, 92)
