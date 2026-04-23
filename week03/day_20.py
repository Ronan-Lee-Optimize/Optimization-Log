# day 20 - mini project prep: while + if/else combined
# opt-log | consistency over perfection.


running = True  # control variable


while running:
    user_input = input("type something (or 'quit' to stop): ")

    
    if user_input == "quit":
        
        running = False       # stop the loop
        print("-")


        
    else:
        print("you typed:", user_input)  # keep looping

# WERE ACTUALLY MAKING ITTTT
