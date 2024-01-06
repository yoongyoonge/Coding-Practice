def solution(code):
    answer = ''
    mode, i = 0, 0
    
    for v in code:
        
        if v == '1':
            mode = 1 - mode # 모드 변경
            i += 1
            continue
        
        if mode == 0: 
            if i % 2 == 0: #짝수 인덱스
                answer += v
            else:
                pass
        else: # mode == 1
            if i % 2 == 1: #홀수 인덱스
                answer += v
        
        #print(i, v, mode)
        i += 1
    
    
    return answer if answer else "EMPTY" # 한 줄로 하는 연습하기


    #return "".join(code.split("1"))[::2] or "EMPTY" # 이 한줄로도 가능
    # 