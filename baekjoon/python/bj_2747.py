n = int(input())
answer = 1

a , b = 0, 1

for i in range(n):
    a, b = b, a+b

print(a)