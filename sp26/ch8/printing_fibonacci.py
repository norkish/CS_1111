# Write a program that generates the Fibonacci sequence up
# to a value given by the user.

stop_value = int(input("Input an upper limit: "))

# create two variables
prev_val = 0
curr_val = 1
str_to_print = str(prev_val)
str_to_print = str_to_print + ", " + str(curr_val)

# for i in range(stop_value):
while curr_val <= stop_value:

    next_val = curr_val + prev_val
    str_to_print = str_to_print + ", " + str(next_val)

    prev_val = curr_val
    curr_val = next_val

# Bonus: print the values all on one line, comma-separated
print(str_to_print)
