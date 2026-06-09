# day SIXSEVEN - review: os module (applied)
# opt-log | consistency over perfection.

import os

print(f"current directory: {os.getcwd()}")
print(f"files in directory: {len(os.listdir())}")

files = os.listdir()
py_files = [f for f in files if f.endswith(".py")]  # filter python files only
print(f"python files: {len(py_files)}")
