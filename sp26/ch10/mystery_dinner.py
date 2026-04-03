# The dinner has three courses:
# 0th course: choose 3 dishes
# 1st course: choose 4 dishes
# 2nd course: choose 3 dishes
# Example: [[1,5,3], [10,2,6,4], [9,8,7]]
# Write a program with a single variable that contains the
# choices for each course (you choose, no input)
food_order = [[1,5,3], [10,2,6,4], [9,8,7]]

# Then for each course, print out A) the course number and
# B) the choices like this:
# Course 0: 1 5 3
for course_num in range(len(food_order)):
    print("Course", str(course_num) + ":", end = "")
    course = food_order[course_num]
    for i in range(len(course)):
        print(" " + str(course[i]), end = "")
    print()

print("\nOr done another way...\n")

for course_num in range(len(food_order)):
    print("Course", str(course_num) + ":", end = "")
    for i in food_order[course_num]:
        print(" " + str(i), end = "")
    print()
  
