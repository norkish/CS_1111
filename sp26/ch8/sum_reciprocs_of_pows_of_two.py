def sum_reciprocals_of_powers_of_two():
    """ Return the sum of reciprocals of powers of 2 """

    sum  = 0
    exponent = 0
    while sum < 2.0:
        sum = sum + 1/2**exponent
        exponent = exponent + 1
        print(exponent, sum)

    return sum


print(sum_reciprocals_of_powers_of_two())
