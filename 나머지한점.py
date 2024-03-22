def solution(v):
    answer = []

    xlist = []
    ylist = []
    
    for i in range(3):
        x,y = v[i]
        xlist.append(x)
        ylist.append(y)
        
    for i in xlist:
        if xlist.count(i)==1:
            answer.append(i)
            break
            
    for i in ylist:
        if ylist.count(i) == 1:
            answer.append(i)
            break

    return answer