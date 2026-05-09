# day 36 - **kwargs
# opt-log | Consistency over perfection.

def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # print each key-value pair

        

profile(name="ronan", goal="master python", days=36)

# GOODMORNIG USA
