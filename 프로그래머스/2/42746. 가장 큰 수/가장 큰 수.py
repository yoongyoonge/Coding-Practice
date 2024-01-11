from itertools import permutations 

def solution(numbers):
    # 순열을 이용하면 numbers의 길이가 10만 이하, 즉 10만 까지도 나올 수 있기 때문에
    # 시간 효율에서 매우 비효율 적이다.
    # 따라서 아래의 코드는 이 문제에 대해서 적절하지 않다.
    '''
    answer = []
    
    p_list = (list(permutations(numbers)))
    answer = [''.join(str(val) for val in p) for p in p_list]
    
    return max(answer)
    '''
    
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer