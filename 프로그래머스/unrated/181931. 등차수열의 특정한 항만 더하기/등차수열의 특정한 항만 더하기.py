def solution(a, d, included):
    answer = 0
    
    true_indices = [index for index, value in enumerate(included) if value]
    
    for v in true_indices:
        answer += a + d * v

    return answer

    # sum(a + i * d for i, f in enumerate(included) if f)
    # f 가 true일때 included에서 인덱스와 값뽑아서 계산