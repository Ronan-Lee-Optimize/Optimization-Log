# day 138 - review: word frequency counter (applied)
# opt-log | consistency over perfection.

sentences = [
    "i have a servere stomach ache",
    "i wanna go home",
    "when does this csat end",
    "i want to have mcdonalds for lunch"
]


word_counts = {}
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


most_common = None
highest = 0
for word, count in word_counts.items():
    if count > highest:
        highest = count
        most_common = word


print()
print(f"most common word: '{most_common}' ({highest} times)")
