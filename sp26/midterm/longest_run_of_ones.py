# find the longest run of 1s in a binary string

binary_string = input("Input a binary string: ")

one_counter = 0
record = 0

# go through one character at a time
for i in range(len(binary_string)):
    # if there's a one, increment our count of ones
    if binary_string[i] == "1":
        one_counter = one_counter + 1
        # and update our record if we've set a record
        if one_counter > record:
            record = one_counter
    else:
        # if there's a zero, reset counter of ones
        one_counter = 0

# print result
print("Longest run of 1s in following string is",record)
print(binary_string)
