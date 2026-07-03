def solution(left, right):
    nums = [num for num in range(left, right+1)]
    answer = 0

    for num in nums:
        count = 2 if (num != 1) else 1
        for i in range(2, num):
            if (num % i) == 0:
                count += 1
        if (count % 2) == 0:
            answer += num
        else:
            answer -= num
    return answer
