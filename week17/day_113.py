# day 113 - new: pandas read_csv and to_csv (applied)
# opt-log | consistency over perfection.
import pandas as pd

data = {"subject": ["math", "english", "korean", "science"],
        "hours": [4, 2, 3, 5]}
df = pd.DataFrame(data)
print(df)


# save the DataFrame to an actual CSV file
df.to_csv("study_log.csv", index=False)
print("saved to study_log.csv!")


# read it back from the file
df_loaded = pd.read_csv("study_log.csv")
print()
print("loaded from file:")
print(df_loaded)
