def solution(n):
    
    if n % 2 == 1: # n이 홀수 
        return sum(range(1, n+1, 2))
    else:
        return sum(x**2 for x in range(2, n+1, 2))