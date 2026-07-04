def solution(num):
    answer = 0
    answer = [num if num != '0' else '1' for num in list(str(num + 1))]
    answer = int(''.join(answer))
    return answer
