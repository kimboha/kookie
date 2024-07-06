# https://www.acmicpc.net/problem/1316
# Init
answer = 0

# Input
n = input() # 1~100

# Func
def is_group_word(group):
    index = 0
    flag = group[0]

    # Find index
    while index < len(group):
        cursor = group[index]

        if flag != cursor:
            break
        
        index += 1

    # Full search
    if index == len(group):
        return True
    
    # Validation sub str
    sub_str = group[index:]
    if sub_str.find(flag) >= 0:
        # Group X
        return False
    
    return is_group_word(sub_str)

# Main
for i in range(0, int(n)):
    word = input()
    if is_group_word(word):
        answer += 1

print(answer)
