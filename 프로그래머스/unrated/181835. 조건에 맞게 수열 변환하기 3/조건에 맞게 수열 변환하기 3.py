def solution(arr, k):
    answer = []
    
    if k % 2 == 1: # k가 홀수 
        answer = [element * k for element in arr]
    else: # k가 짝수 
        answer = [element + k for element in arr]
    
    return answer