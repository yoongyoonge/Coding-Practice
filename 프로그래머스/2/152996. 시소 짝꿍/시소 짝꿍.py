from collections import Counter

def solution(weights):
    answer, counter = 0, Counter(weights) # 각 무게에 대한 빈도수가 저장
    
    for i in counter:
        if counter[i] > 0: # 빈도수가 0보다 큰 경우
            # 무게 i 에 대한 빈도수를 사용하여 nC2계산, nC2: 무게 i의 빈도수에서 2개를 선택하는 조합의 수
            answer += counter[i] * (counter[i] - 1) // 2 
            # 무게 i에 대한 빈도수와 무게 i * 3 // 2에 대한 빈도수를 곱, // 연산자는 나눗셈 후 소수점을 버리고 정수만을 반환
            answer += counter[i] * counter[i * 3 / 2]
            # 무게 i에 대한 빈도수와 무게 i*2에 대한 빈도수를 곱 
            answer += counter[i] * counter[i * 2]
            # 무게 i에 대한 빈도수와 무게 i * 4 // 3에 대한 빈도수를 곱 
            answer += counter[i] * counter[i * 4 / 3]
    
    return answer