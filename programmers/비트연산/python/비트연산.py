def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        mapped = ""
        a = bin(arr1[i] | arr2[i])[2:]
        if len(a) < n:
            mapped += (" " * (n - len(a)))
        for j in range(len(a)):
            if a[j] == "1":
                mapped += "#"
            else:
                mapped += " "
        answer.append(mapped)
    return answer