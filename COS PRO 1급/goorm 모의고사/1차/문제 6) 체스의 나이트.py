def check(pos1, pos2):
    if (0 <= pos1 <= 7) and (0 <= pos2 <= 7):
        return 1
    else:
        return 0


def solution(pos):
    answer = 0
    pos = [ord(pos[0])-65, int(pos[1]) - 1]
    vecs = [[2, 1], [-2, 1], [1, 2], [-1, 2]]
    vecs += [[-vec[0], -vec[1]] for vec in vecs]
    pos_hubos = [[pos[0] + vec[0], pos[1] + vec[1]] for vec in vecs]
    for pos_hubo in pos_hubos:
        answer += check(pos_hubo[0], pos_hubo[1])
    return answer
