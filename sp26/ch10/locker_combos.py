# You are in charge of keeping track of the
# codes for a set of lockers.
# Write a program that keeps one list
# with all of the codes (you set the codes)
# Each code should be a list of three numbers
code_list = [[1,2,3], [3,2,1], [2,1,3]]

# Then print out each locker number with its code to look like this:
# Locker 0 has combo 4 – 6 - 2
for locker_num in range(len(code_list)):
    print("Locker", locker_num, "has combo", end="")
    lock_combination = code_list[locker_num]
    for i in range(len(lock_combination)):
        if i != 0:
            print(" -", end="")
        print(" " + str(lock_combination[i]), end = "")

    print()
