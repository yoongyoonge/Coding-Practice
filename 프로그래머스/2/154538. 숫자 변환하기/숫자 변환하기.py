def solution(x, y, n):
    answer = 0
    
    if x == y:
        return 0
    
    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    
    for cn in range(x, y+1):
        if cn * 2 <= y:
            dp[cn * 2] = min(dp[cn * 2], dp[cn] + 1)
            
        if cn * 3 <=y:
            dp[cn * 3] = min(dp[cn * 3], dp[cn] + 1)
        
        if cn + n <= y:
            dp[cn + n] = min(dp[cn + n], dp[cn] + 1)
            
    if dp[y] == float('inf'):
        return -1
    
    return dp[y]