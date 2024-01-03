def solution(s, skip, index):
    
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in alpha:
        if i in skip:
            alpha = alpha.replace(i,'')
            
    for i in s:
        answer += alpha[(alpha.index(i)+index)%len(alpha)]

    return answer