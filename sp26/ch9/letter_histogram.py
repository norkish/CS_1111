import string


def count(text, a_char):
    lettercount = 0
    for c in text:
        if c == a_char:
            lettercount = lettercount + 1
    return lettercount

# Write a program that takes an input string
input_string = input("Input: ")
# from the user, converts the string to lower
input_string = input_string.lower()
# case, and uses the function above to
# report a histogram (i.e., letter count) for each of the letters a to z

for c in string.ascii_lowercase:
    print(c, count(input_string, c) * "*")
