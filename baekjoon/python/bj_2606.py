# first try
# 예제입력 성공
T = int(input())

C = int(input())

infect = [int(v) for v in list(input().split())]

for i in range(C - 1):
    con = [int(v) for v in list(input().split())]
    
    while con:
        b = con.pop(0)
        if b in infect:
            infect.append(b)
            infect.append(con.pop())
        else:
            if con[0] in infect:
                infect.append(b)
                infect.append(con.pop())
            else:
                con.pop()

print(len(set(infect)) -1)

