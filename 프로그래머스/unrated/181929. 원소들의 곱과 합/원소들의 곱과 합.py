def solution(num_list):
    
    m = 1 # 모든 원소들의 곱
    for n in num_list:
        m *= n
    
    return 1 if m < sum(num_list)**2 else 0