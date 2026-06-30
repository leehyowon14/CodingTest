def solution(wallpaper):
    answer = [-1, 50, -1, 0]  # y1 x1 y2 x2
    line_length = len(wallpaper[0])
    for idx, line in enumerate(wallpaper):
        line = list(line)
        if "#" in line:
            if answer[0] == -1:
                answer[0] = idx  # 드래그되어야 할 첫번째 라인(y1)
            answer[1] = min(answer[1], line.index("#"))  # 시작 x 좌표(x1)
            line.reverse()
            answer[3] = max(answer[3], line_length - line.index("#"))  # 끝 x 좌표
            last_line = idx  # 마지막으로 파일이 등장한 라인
    answer[2] = last_line + 1  # 끝 y좌표(y2)

    return answer
