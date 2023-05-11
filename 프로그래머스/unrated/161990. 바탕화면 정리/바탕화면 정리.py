# wallpaper : 바탕화면 상태(1차원 배열, 각 원소는 문자열임)
# .은 빈칸 #은 파일 존재 => #을 다 지우고 싶음
def solution(wallpaper):
    point_x, point_y = [], []
    
    for index_line, line in enumerate(wallpaper):
        for index_pt, pt in enumerate(line):
            if pt == '#':
                if index_line not in point_x:
                    point_x.append(index_line)
                if index_pt not in point_y:
                    point_y.append(index_pt)
            # print(index_line, index_pt, pt)
    # print('x : ', point_x, min(point_x), max(point_x))
    # print('y : ', point_y, min(point_y), max(point_y))
    # answer = [] # 시작점(x, y), 끝점(x, y), 시작점 < 끝점
    answer = [min(point_x), min(point_y), max(point_x)+1, max(point_y)+1]
    return answer