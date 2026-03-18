
quotient = int(input("Gimme a number in decimal: "))

binary_string = ""

while quotient != 0:
    # if when we divide by two there is a remainder
    if quotient % 2 == 1:
        # tack a "1" to the left side of the string
        binary_string = "1" + binary_string
    else:
        # otherwise tack a "0" on to the left side
        binary_string = "0" + binary_string

    quotient = quotient // 2

print(binary_string)
