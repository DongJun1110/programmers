from collections import deque

def solution(board):
    
    n,m = len(board), len(board[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    dist = [[9999999 for _ in range(m)] for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i,j,0))
                break
                
    while q:
        x,y,result = q.popleft()
        
        if board[x][y] == 'G':
            return result
    
        for i in range(4): 
            nx = x
            ny = y 
            
            while 0<=dx[i]+nx<n and 0<=dy[i]+ny<m and board[nx+dx[i]][ny+dy[i]]!='D':
                nx += dx[i]
                ny += dy[i]
                
            if dist[nx][ny] > result+1:
                dist[nx][ny] = result+1
                q.append((nx,ny,result+1))
                
    
    return -1


    