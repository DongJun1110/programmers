def solution(picks, minerals):
    answer = 0
    
    avaliable = (sum(picks)*5)
    if len(minerals) > avaliable:
        minerals = minerals[:avaliable]
    
    newnerals = [[0,0,0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            newnerals[i//5][0] += 1
        elif minerals[i] == 'iron':
            newnerals[i//5][1] += 1
        else:
            newnerals[i//5][2] += 1
    
    newnerals.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    
    for mineral in newnerals:
        d, i, s = mineral
        
        if picks[0] > 0:
            answer += (d+i+s)
            picks[0] -= 1
            continue
        elif picks[1] > 0:
            answer += (5*d + i +s)
            picks[1] -= 1
            continue
        elif picks[2] > 0:
            answer += (25*d + 5*i + s)
            picks[2] -= 1
            continue
    
    return answer