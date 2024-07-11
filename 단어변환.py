from collections import deque
def solution(begin, target, words):
    
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        
        for i in range(len(words)):
            if onechar(word, words[i]) and not visited[i]:
                q.append((words[i],cnt+1))
                visited[i] = True
    return 0

def onechar(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    
    return False
