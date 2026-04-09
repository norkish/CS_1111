a = [1,2,3,4]
b = a
b[0] = "hat"
print(a)



c = [1,2,3,4,5,6,7]
d = c[:]

print(c == d)
print(c is d)

d[0] = "hat"

print(c)
print(d)
