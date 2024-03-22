import heapq

def solution(S, K):
    answer = 0
    heapq.heapify(S)
    
    while S[0] < K:
        result = heapq.heappop(S)+(heapq.heappop(S)*2)
        heapq.heappush(S,result)
        answer += 1
        if len(S) == 1 and S[0]<K:
            return -1
    
    return answer
    