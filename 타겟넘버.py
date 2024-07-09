from collections import deque
def solution(numbers, target):
    
    answer = 0
    temp = [0]
    
    for i in range(len(numbers)):
        result = []
        while temp:
            x = temp.pop()
            result.append(x+numbers[i])
            result.append(x-numbers[i])
        temp = result
        result = []
    
    for num in temp:
        if num == target:
            answer += 1
                
    return answer
