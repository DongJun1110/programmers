def solution(name, yearning, photo):
    answer = []
    for group in photo:
        result = 0
        for  member in group:
            if member in name:
                result += yearning[name.index(member)]
        answer.append(result)
    return answer

