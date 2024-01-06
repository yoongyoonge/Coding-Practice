def solution(a, b):
    answer = 0
    
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    if max(ab, ba) == ab:
        answer = ab
    else:
        answer = ba
        
    # answer = max(int(f"{a}{b}"), int(f"{b}{a}"))
    
    return answer