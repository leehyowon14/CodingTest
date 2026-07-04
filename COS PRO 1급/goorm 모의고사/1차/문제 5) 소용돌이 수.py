def solution(n):
    answer = 0
    grid = [[0 for i in range(n)] for j in range(n)]
    r = 0
    r_max = n
    r_min = 0
    c = 0
    c_max = n
    c_min = 0
    num = 1
    while (r_min <= r_max) and (c_min <= c_max):
        for r_ in range(r_min, r_max):
            grid[c][r_] = num
            num += 1
            r = r_
        c_min += 1
        for c_ in range(c_min, c_max):
            grid[c_][r] = num
            num += 1
            c = c_
        r_max -= 1
        for r_ in range(r_max-1, r_min-1, -1):
            grid[c][r_] = num
            num += 1
            r = r_
        c_max -= 1
        for c_ in range(c_max-1, c_min-1, -1):
            grid[c_][r] = num
            num += 1
            c = c_
        r_min += 1

    for i in range(n):
        answer += grid[i][i]
    return answer
