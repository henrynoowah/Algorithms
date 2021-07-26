def solution(n):
    
    listn = list(str(n))
    return int(''.join(sorted(listn, reverse = True)))




#    listn = list(str(n))
#    문자열로 만들고 리스트화
#    sorted(listn, reverse = True)
#    sorted() 함수 사용해서 오름차순 정렬
#    ''.join(listn)
#    문자열에다 리스트 조인
#    int(listn)
#    다시 숫자로 변환