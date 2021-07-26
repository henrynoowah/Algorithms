def solution(x):
    answer = True
    indexSum = 0
    arr = list(f'{x}')
    for i in arr:
        indexSum += int(i)
        
    if x % indexSum:
        return False
    else:
        return True