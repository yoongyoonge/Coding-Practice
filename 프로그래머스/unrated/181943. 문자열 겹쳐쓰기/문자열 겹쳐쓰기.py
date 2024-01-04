def solution(my_string, overwrite_string, s):
    answer = ''
    
    if s < 0 or s >= len(my_string):
        print("인덱스 에러")
        return my_string
    
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    
    return answer