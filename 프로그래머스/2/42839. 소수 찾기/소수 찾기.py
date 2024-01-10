import math
from itertools import permutations

def is_prime(n):
    # 이 함수는 소수를 판별하는 함수입니다.
    # 2보다 작으면 소수가 아니고
    if n < 2:
        return False
    elif n == 2: # 2는 소수
        return True
    
    # 2보다 크면 2부터 제곱근 까지 나누어보기
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False #나누어 떨어지면 소수가 아님
        
    return True


def solution(numbers):
    
    # 카드로 만들 수 있는 모든 조합 
    # permutation은 자리수를 유지, combination은 여러 가지 자리수를 만들어야 할 때 사용
    
    n = len(numbers)
    per_list = []
    
    for r in range(1, n+1):
        for p in permutations(numbers, r):
            per_list.append(''.join(p))

    # 문자열을 숫자로 변환 및 중복제거
    per_int_list = [int(x) for x in per_list]
    per_int_list = set(per_int_list)
    
    count = 0
    for val in per_int_list:

        if is_prime(val):
            count += 1
        else:
            pass
        
    return count