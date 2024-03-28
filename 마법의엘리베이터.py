def solution(s):
    answer = 0
    
    while(s):
        num = s%10
        if num>5:
            answer += (10-num)
            s += 10
        elif num<5:
            answer += num
        else:
            if (s//10)%10>4:
                s+=10
            answer += 5
        s //= 10
    
    return answer