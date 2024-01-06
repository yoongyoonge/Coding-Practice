def solution(num, n):
    
    if num % n == 0:
        return 1
    else:
        return 0
    
    # return int(not(num % n))