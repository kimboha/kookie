# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    halfLength = int(len(s) / 2)
    
    for i in range(1, halfLength + 1):
        j = i
        le = len(s)
        piece = s[0:i]
        cnt = 1

        while j < len(s):
            if s[j:j+i] == piece:
                le -= i
                cnt += 1
            elif cnt > 1:
                le += len(str(cnt))
                cnt = 1

            piece = s[j:j+i]
            j += i

        if cnt > 1:
            le += len(str(cnt))

        if le < answer:
            answer = le
            
    return answer
