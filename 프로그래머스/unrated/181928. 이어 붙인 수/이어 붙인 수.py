def solution(num_list):
    
    odd_str, even_str = "", ""
    
    for n in num_list:
        if n % 2 == 0: # n이 짝수일 경우 
            even_str += str(n)
        else: 
            odd_str += str(n)
    
    return int(even_str) + int(odd_str)