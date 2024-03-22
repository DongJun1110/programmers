def solution(phone_book):
    phone_book.sort()
    
    for i in range(0,len(phone_book)-1):
        if len(phone_book[i]) > len(phone_book[i+1]):
            continue
        str = phone_book[i+1]
        if str[:len(phone_book[i])] == phone_book[i]:
            return False
    
    return True