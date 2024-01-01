def solution(t, p):
    
    answer = 0
    num = len(t)-len(p)+1
    
    for i in range(num):
        str = int(t[i:i+len(p)])
        if str <= int(p): answer+=1
    
    return answer