from heapq import heappush, heappop

def change_time(start, end):
    start = int(start[0:2])*60 + int(start[3:])
    end = int(end[0:2])*60 +int(end[3:])
    return (start,end)
    
def solution(book_time):
    answer = 1

    for index, item in enumerate(book_time):
        book_time[index] = change_time(item[0],item[1])
    book_time.sort()
    heap = []
    for start, end in book_time:
        if not heap:
            heappush(heap, end+10)
            continue
        if heap[0] <= start:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,end+10)

    return answer