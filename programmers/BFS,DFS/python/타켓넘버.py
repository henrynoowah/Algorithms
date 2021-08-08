# numbers = [1,1,1,1,1]
# target = 3

def solution(numbers, target):

  count = 0

  arrA = [0]
  for num1 in numbers:
    arr = []
    for num2 in arrA:
      arr.append(num2 + num1)
      arr.append(num2 - num1)

    arrA = arr

  print(arrA)

  for i in arrA:
    if i == target:
      count += 1

  # print(count)

# solution(numbers, target)

