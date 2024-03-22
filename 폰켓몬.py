def solution(nums):
    
    leng = len(nums)//2
    newleng = len(set(nums))
    
    if newleng >= leng: 
        answer = leng
    else:
        answer = newleng
        
    return leng if newleng >= leng else newleng
    
