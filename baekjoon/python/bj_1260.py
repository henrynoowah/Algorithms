arr = [int(v) for v in list(input().split())]

N = arr[0] # 4
M = arr[1] # 5
V = arr[2] # 1

path =[]
stack = []

for i in range(M):

    next = V

    p = [int(v) for v in list(input().split())]


    else:
        stack.append(p)

    print(path)
    print(stack)

#   [[1, 2], [1, 3], [1, 4]]
#   [[2, 4], [3, 4]]

# dequeue rotate 사용??
#  
