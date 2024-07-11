from collections import deque

def solution(n, computers):
    
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    answer = 0
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        computers[x][y] = 0
        computers[y][x] = 0
        while q:
            x,y = q.popleft()
            for i in range(n):
                if computers[i][x] == 1:
                    q.append((i,x))
                    computers[i][x] = 0
                    computers[x][i] = 0 
                
                if computers[i][y] == 1:
                    q.append((i,y))
                    computers[i][y] = 0
                    computers[y][i] = 0 
        return 1

  for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                answer += bfs(i,j)
    
    return answer
