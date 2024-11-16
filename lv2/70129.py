# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    # Init
    transferCnt = 0
    zeroCnt = 0
    x = s
    
    while len(x) > 1:
        transferCnt += 1
        zeroCnt += len(x)

        # Remove zero
        c = x.count('1')
        x = '1' * c
        zeroCnt -= c

        # length to binary
        x = str(bin(c))[2:]
    
    return [transferCnt, zeroCnt]
