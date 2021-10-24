ticekts = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets =  [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]



def solution(tickets):
    # tickets.sort(reverse=True)
    answer = []
    routes = {}
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    # routes = {
    #   'ICN': ['SFO', 'ATL'], 
    #   'SFO': ['ATL'], 
    #   'ATL': ['ICN', 'SFO']
    # }
    # print(routes)

    # 역순정렬
    for r in routes.values():
        r.sort(reverse=True)
    # routes = {
    #   'ICN': ['SFO', 'ATL'], 
    #   'SFO': ['ATL'], 
    #   'ATL': ['SFO', 'ICN']}
        


    print(routes)
    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    st = ["ICN"] 
    answer = []
    while st:
        top = st[-1]
        print(top)
        # routes의 연결된 경로가 없을 때 티켓을 다 연결하지 못한 경우 & 모든 경로가 연결되어있지 않을 때
        # 마지막 경로들의 연결지점이라는 뜻
        if top not in routes or len(routes[top]) == 0:
            answer.append(st.pop())
        # 안에 경로가 있을때 경로를 st에 추가 
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
        print(st)
        print(answer)
        print(routes)
        print("-" * 40)
    

    
    # while st:
    #     top = st[-1]
    #     if top in routes and len(routes[top]) != 0:
    #         answer.append(st.popleft())
    #     else:
    #         st.append(routes[top].pop())
            
            
        # for loc, next in routes.items():
        #     print(loc, next)
        #     if loc == top:
        #         top = next[0]
        #         print(top)
        #         st.append(next.pop(0))
        
        
    # ['ICN', 'SFO', 'ATL', 'ICN', 'ATL', 'SFO']
    # 결과를 만들었지만 반복문을 중지시키는 조건을 어떻게 만들까...?

    # alphabet 우선순위로 갔을 때 여행경로를 다 지나는지 확인 필요!
    return answer

# tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# # [['ICN', 'B'], ['ICN', 'A'], ['D', 'A'], ['B', 'ICN'], ['A', 'D']]
# # [['SFO', 'ATL'], ['ICN', 'SFO'], ['ICN', 'ATL'], ['ATL', 'SFO'], ['ATL', 'ICN']]

# def solution(tickets):
#     tickets.sort(reverse=True)
#     # sorting 을 하는 이유는 뭘까?
#     # [['SFO', 'ATL'], ['ICN', 'SFO'], ['ICN', 'ATL'], ['ATL', 'SFO'], ['ATL', 'ICN']]
#     print(tickets)
#     routes = {}
    
#     for t1, t2 in tickets:
#         if t1 in routes:
#             routes[t1].append(t2)
#         else:
#             routes[t1] = [t2]
    
#     # print(routes)
#     # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
#     # {'SFO': ['ATL'], 'ICN': ['SFO', 'ATL'], 'ATL': ['SFO', 'ICN']}

#     st = ['ICN']
#     ans = []
    
#     while st:
#         top = st[-1]
#         ['ICN']
#         # KeyError 'IAD'를 방지하기위해 not it routes 조건 추가
#         # 2번 쨰 조건을 위한 조건문
#         # routes[현재 루트]에 다음 경로가 없다면 현재루트를 ans에 추가하며 마무리
#         if top not in routes or len(routes[top])==0:
#             ans.append(st.pop())
#         # key 값에 list 가 바어있지 않다면 다음 route로 append
#         else:
#             st.append(routes[top].pop())
#         # print(ans)
#         # print(st)
#     ans.reverse()
#     print(ans)
#     return ans

solution(tickets)