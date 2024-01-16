def solution(number, limit, power):

    answer = []
    
    for i in range(1,number+1):
        divnum = 0
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                divnum += 1
                if j**2!=i:
                    divnum+=1
        answer.append(power) if divnum>limit else answer.append(divnum)
    
    return sum(answer)