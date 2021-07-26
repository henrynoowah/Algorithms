# My Solution
def solution(s):
    
    while len(s) == 4 or len(s) == 6:
        if s != s.upper():
            return False
        elif s != s.lower():
            return False
        else:
            return True
    
    return False


# Try 사용
def solution(s):
    try:
        if type(int(s)) == int and 4 == len(s) or 6 == len(s):
            return True
        else:
            return False
    except:       
        return False


# isdigit() 사용
def solution(s):
    return s.isdigit() and len(s) in (4, 6)