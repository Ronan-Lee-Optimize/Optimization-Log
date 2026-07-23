# day 111 - review: numpy and pandas together (applied)
# opt-log | consistency over perfection.
import numpy as np
import pandas as pd

data = {"subject": ["math", "english", "korean", "science"],
        "hours": [5, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)
print()


# pandas column to numpy array
hrs_array = df["hours"].to_numpy()
print(f"as numpy array: {hrs_array}")



# numpy functions on it
print(f"mean: {hrs_array.mean():.1f}")
print(f"above average: {hrs_array[hrs_array > hrs_array.mean()]}")



# numpy array back into a new pandas column
df["hours_tripled"] = np.array(df["hours"]) * 3
print()
print(df)
