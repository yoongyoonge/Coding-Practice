def solution(park, routes):
    
    # 시작 위치를 찾기 
    start_pos = None
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start_pos = (i, j)
                break
                
    # 이동 방향 좌표화
    # 주의할 것: 공원의 가로 길이가 W, 세로길이가 H라고 할 때 우측 하단이 (H-1, W-1)로 일반적인 x, y가 아님
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    current_pos = start_pos # 움직인 좌표 초기 설정 값
    
    # 로봇강아지 이동
    for step in routes:
        
        # 이동을 위한 x, y 추출
        direction, distance_s = step.split()
        distance = int(distance_s)
        dx, dy = directions[direction]
        
        # 이동 시키기
        tmp_pos = current_pos # 이동하지 않을 때를 대비하여 임시 저장
        for k in range(distance): 
            
            # 이동 후 좌표
            # 장애물이 있나 확인해야하기 때문에 한번에 이동하지 않고 1씩 이동
            new_pos = (current_pos[0] + dx, current_pos[1] + dy) 
            
            # new_pos 가 유효한지 확인
            # 공원 영역 안에 위치하는지, 이동한 위치는 장애물이 있는 위치는 아닌지 확인
            if (
                0 <= new_pos[0] < len(park) and 
                0 <= new_pos[1] < len(park[0]) and
                park[new_pos[0]][new_pos[1]] in ('O', 'S') # O뿐만 아니라 S도 갈 수 있는 지역
            ):
                current_pos = new_pos # 유효하면 이동
            else:
                if k <= distance: # 거리를 다 채우기 이전에 이동한 값이 유효하지 않다면
                    current_pos = tmp_pos # 이전 값으로 되돌리기
                break # 아니면 이동하지않고 다음 반복문으로 진행
    
    return current_pos