def solution(a, b):
    answer = 0
    
    ab = int(f"{a}{b}")
    
    answer = max(ab, 2*a*b)
    
    return answer