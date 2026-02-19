def sqrt(a):
    assert type(a) == int, "Input to sqrt function not an integer"
    return a ** 0.5

answer = sqrt("Hello")
print("Answer is:", answer)
