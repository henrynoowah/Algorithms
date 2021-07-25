def solution(n):

    i = 1

    while True:
        if pow(i, 2) == n:
            return pow(i + 1, 2)
        
        elif i > n:
            return -1
        
        i += 1
