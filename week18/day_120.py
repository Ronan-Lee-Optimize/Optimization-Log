# day 120 - review: csv read/write and concat (applied)
# opt-log | consistency over perfection.
import pandas as pd


# create a small practice df and save it
data = {"subject": ["math", "english"], "hours": [3, 2]}
df = pd.DataFrame(data)
df.to_csv("practice_log.csv", index=False)
print("saved practice_log.csv")


# load it back
df_loaded = pd.read_csv("practice_log.csv")
print(df_loaded)
print()


# append new rows with concat
new_data = {"subject": ["korean", "science"], "hours": [4, 1]}
df_new = pd.DataFrame(new_data)
df_combined = pd.concat([df_loaded, df_new], ignore_index=True)


df_combined.to_csv("practice_log.csv", index=False)
print("after appending:")
print(df_combined)
