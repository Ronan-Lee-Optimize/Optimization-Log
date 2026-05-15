# day 42 - review: **kwargs (applied)
# opt-log | consistency over perfection.

def student_profile(**kwargs):
    print("--- profile ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # print each key-value pair

        

student_profile(name="ronan", goal="be a god of coding", days=42, language="python")

# GAWD DAYUM END OF WEEK SIX
