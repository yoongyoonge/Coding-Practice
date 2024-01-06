def solution(a, d, included):
    answer = 0
    
    true_indices = [index for index, value in enumerate(included) if value]
    
    for v in true_indices:
        answer += a + d * v

    return answer