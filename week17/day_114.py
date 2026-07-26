# day 114 - new: appending new data to an existing csv (applied)
# opt-log | consistency over perfection.
import pandas as pd

# load yesterday's saved data
df_old = pd.read_csv("study_log.csv")
print("existing data:")
print(df_old)


# today's new data (same columns)
new_data = {"subject": ["math", "english", "korean", "science"],
            "hours": [3, 4, 2, 3]}
df_new = pd.DataFrame(new_data)


# combine old and new rows together
df_combined = pd.concat([df_old, df_new], ignore_index=True)
print()
print("combined data:")
print(df_combined)


# save the combined version back to the file
df_combined.to_csv("study_log.csv", index=False)
print()
