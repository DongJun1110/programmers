def solution(s):
    result = []
    for i in s:
        while result and i > result[-1]:
            result.pop()
        result.append(i) 
    return ''.join(result)

