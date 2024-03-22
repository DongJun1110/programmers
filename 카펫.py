def solution(b, y):
    
    hor, ver = 0,0
    for i in range(1,y+1):
        if y%i == 0:
            hor = y//i
            ver = i
            if (hor+2)*2 + ver*2 == b:
                return [hor+2,ver+2]
    
