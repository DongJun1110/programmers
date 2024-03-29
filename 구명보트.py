from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    
    while q:
        if q[0]+q[-1] <= limit and len(q)>1:
            q.popleft()
            q.pop()
            answer += 1
        else:
            q.pop()
            answer += 1
    
    return answer
    
