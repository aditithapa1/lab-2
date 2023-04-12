num_rows = 8
for i in range(num_rows):
    if i == 0:
        print("")
    else:
        print("#", end="")
        for j in range(1, i):
            print(" ", end="")
        print("#")