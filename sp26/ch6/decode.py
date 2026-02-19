# Write a program that does the following:
# Solicit the user for an integer for the number 𝑛 of characters to decode
# Converts the user's input into an int type
n = int(input("How many characters in your message? "))

# Uses an assert statement to ensure the integer is non-negative (how can we do this only using the '==' operator?)
assert n == abs(n), "input number is negative"

message = ""
# For 𝑛 non-negative integer codes,
for i in range(n):
    # Solicit the user for an integer for the next code
    # Converts the user's input into an int type
    next_char_int = int(input("Next character's ASCII number: "))
    # Use an assert statement to ensure the integer is non-negative
    assert next_char_int == abs(next_char_int), "input number is negative"

    # Decode each character using the chr() function to convert from an integer to its ASCII equivalent
    next_char = chr(next_char_int)
    # Concatenates the characters into a single string
    # print(next_char_int,"in ASCII is", next_char)
    message = message + next_char

# Prints out the user's decoded message
print(message)
