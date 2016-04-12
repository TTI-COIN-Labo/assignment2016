import sys
with open(sys.argv[1], mode='r') as file:
    for line in file:
        if sys.argv[2] in line:
            print(line, end="")
