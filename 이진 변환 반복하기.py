def solution(s):
    zerocnt = 0
    while True:
        if s=='1':
            break
        zerocnt += s.count('0')
        cnt += 1
        s = bin(len(s.replace('0','')))[2:]
    return [cnt, zerocnt]

