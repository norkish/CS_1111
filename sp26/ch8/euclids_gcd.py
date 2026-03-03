# define a function that takes 2 integers, a and b, and returns their GCD
def compute_gcd(a, b):
    r = a - b * (a // b)
    while r != 0:
        a = b
        b = r
        r = a - b * (a // b)

    return b

gcd = compute_gcd(45,15)
print("GCD is ", gcd)

gcd = compute_gcd(15,45)
print("GCD is ", gcd)

gcd = compute_gcd(157,63)
print("GCD is ", gcd)

gcd = compute_gcd(300,175)
print("GCD is ", gcd)
