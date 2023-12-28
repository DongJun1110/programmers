def solution(today, terms, privacies):
    
    answer = []
    di = {}
    
    today = list(map(int,today.split('.')))
    
    for term in terms:
        s,m = term.split()
        di[s] = int(m)*28
    
    for i in range(len(privacies)):
        date, sort = privacies[i].split()
        date = list(map(int,date.split('.')))
        year = (today[0] - date[0]) *28*12
        month = (today[1] - date[1]) *28
        day = today[2] - date[2] 
        
        if di[sort] <= year+month+day:
            answer.append(i+1)
        
    return answer