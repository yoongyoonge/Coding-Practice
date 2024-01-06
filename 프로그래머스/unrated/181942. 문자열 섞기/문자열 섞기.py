def solution(str1, str2):
    answer = ''
    
    len_a, len_b = len(str1), len(str2)
    max_len = max(len_a, len_b)
    
    for i in range(max_len):
        if i < len_a:
            answer += str1[i]
        if i < len_b:
            answer += str2[i]
    
    '''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    '''
    
    
    return answer