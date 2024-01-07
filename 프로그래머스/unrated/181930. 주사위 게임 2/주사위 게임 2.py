def solution(a, b, c):
    answer = 0
    
    # set()이 클래스이기 때문에, set(a,b,c)일 경우 
    # a는 set의 첫번째 파라미터, b는 두번째 파라미터, c는 세번째 파라미터로 인식
    # 따라서 set([a,b,c])처럼 list로 감싸서 넘겨주어야함
    l = len(set([a, b, c])) 
    
    if l == 3: # 중복되지 않을 경우 
        answer = a + b + c
    elif l == 2: # 하나가 중복될 경우 
        answer = (a + b + c)*(a**2 + b**2 + c**2)
    elif l == 1: # 모두 중복될 경우 
        answer = (a + b + c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3) # 3*a*3*(a**2)*3*(a**3)
    
    return answer