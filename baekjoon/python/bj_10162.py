import sys

A, B, C = 300, 60, 10
T = int(sys.stdin.readline())

if T % C != 0:
    print(-1)
else:
    a = T // A 
    # a = 0
    b = T % A
    # b = 100
    t = b
    # t = 100

    b = t // B
    # b = 1
    c = t % B
    # c = 100 % 60 = 40
    t = c
    # t = 40

    c = t // C
    # c = 40 // 10 = 4
    # t = t % C
    # t = 

    print(f'{a} {b} {c}')
    
