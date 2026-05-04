# day 31 - file read/write
# opt-log | consistency over perfection.

# write to a file
with open("log.txt", "w") as f:
    
    f.write("day 31 - file practice\n")  # write a line
    
    f.write("ronan was here\n")



# read from a file
with open("log.txt", "r") as f:
    
    content = f.read()
    
    print(content)  # print file contents
