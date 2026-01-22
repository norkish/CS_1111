# Live Coding demonstration—Write a program
# with variables representing
# the miles driven on 3 different days (you choose the miles).
# Create a 4th variable that is updated to reflect the total
# count of all 3 variables. Print out all four variables.

# Copy and adapt your program summing the mileage so that the
# 3 daily mileage variables are set by user input.

total_miles = 0.0   # accumulator variable

day_1_mileage = float(input("How many miles did you drive on Day 1? "))
total_miles = total_miles + day_1_mileage # update

day_2_mileage = float(input("How many miles did you drive on Day 2? "))
total_miles = total_miles + day_2_mileage # update

day_3_mileage = float(input("How many miles did you drive on Day 3? "))
total_miles = total_miles + day_3_mileage # update

print("Total miles:", total_miles, "miles")
