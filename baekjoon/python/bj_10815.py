N = int(input())
arrN = sorted([int(i) for i in input().split()]) 

M = int(input())
arrM = [int(i) for i in input().split()]


# N = 5
# arrN = sorted([6, 3, 2, 10, -10]) 

# M = 8
# arrM = [10, 9, -5, 2, 3, 4, 5, -10]

arrA = []

for num in arrM:
  
  left = 0
  right = len(arrN) - 1
  count = 0
  
  while left <= right:

    mid = (left + right) // 2

    if num == arrN[mid]:
      count += 1
      break
    elif num > arrN[mid]:
      left = mid + 1
    else:
      right = mid - 1
    
  arrA.append(count)


print(" ".join(list(map(str, arrA))))
# answer = " ".join(list(map(str, arrA)))

