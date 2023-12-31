def solution(keymap, targets):

    answer = []
    dict = {}
    
    for key in keymap:
        for e in key:
            if e not in dict:
                dict[e] = key.index(e)+1
            elif key.index(e)+1 < dict[e]:
                dict[e] = key.index(e)+1
    
    for target in targets:
        sum = 0
        for e in target:
            num = dict.get(e)
            if num == None:
                sum = -1
                break
            sum += num
        answer.append(sum)
    
    return answer