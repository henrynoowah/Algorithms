def factorial(num):
    fct = 1
    for i in range(num, 1, -1):
        fct *= i
    return fct

N = int(input())
print(factorial(N))
