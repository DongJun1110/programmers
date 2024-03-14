from collections import deque
def solution(maps):
    answer = []
    
    n,m = len(maps), len(maps[0])
    
    #상하좌우
    dir = [(0,-1), (0,1), (-1,0), (1,0)]
    visited = [[False]*m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 'X' or visited[x][y]:
                continue
                
            q = deque()
            q.append((x,y))
            visited[x][y] = True
            
            result = 0
            
            while q:
                nx, ny = q.popleft()
                
                result += int(maps[nx][ny])
                
                for dx,dy in dir:
                    if 0<= nx+dx < n and 0<= ny+dy < m and maps[nx+dx][ny+dy] != 'X' and visited[nx+dx][ny+dy]==False:
                        q.append((nx+dx, ny+dy))
                        visited[nx+dx][ny+dy] = True
            if result:
                answer.append(result)
    
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
            
    
        
    
