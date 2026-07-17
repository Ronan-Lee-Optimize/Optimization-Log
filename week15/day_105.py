# day 105 - new: numpy and pandas together (applied)
# opt-log | consistency over perfection.
import numpy as np
import pandas as pd

data = {"subject": ["math", "english", "korean", "science"],
        "hours": [4, 2, 3, 5]}
df = pd.DataFrame(data)
print(df)
print()

# a pandas column can be converted straight into a numpy array
hrs_array = df["hours"].to_numpy()
print(f"as numpy array: {hrs_array}")
print(f"type: {type(hrs_array)}")

# now numpy functions work directly on it
print(f"mean: {hrs_array.mean():.1f}")
print(f"days above average: {hrs_array[hrs_array > hrs_array.mean()]}")

# numpy array can also become a new pandas column
df["hours_doubled"] = np.array(df["hours"]) * 2
print()
print(df)

# week 15 done
