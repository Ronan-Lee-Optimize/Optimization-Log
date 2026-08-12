# day 130 - bridge week: text/word frequency counter (applied)
# opt-log | consistency over perfection.

print("=== word frequency counter ===")
print()

sentences = [
    "i study math every day",
    "i also study english every week",
    "math is really hard but i keep going fire"
]


word_counts = {}


# break each sentence into words and count them
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1


print("word frequency:")
for word, count in word_counts.items():
    print(f"{word}: {count}")


# find the most common word by hand (no numpy, no max shortcut on a dict directly)
most_common = None
highest = 0
for word, count in word_counts.items():
    if count > highest:
        highest = count
        most_common = word


print()
print(f"most common word: '{most_common}' ({highest} times)")
