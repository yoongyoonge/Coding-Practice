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

# 이런풀이도 있다 
'''
    from itertools import combinations
    from collections import Counter
    
    cnt = 0
    weights = Counter(weights)
    for a, b in combinations(weights.keys(), 2): # 서로 다른 무게, 딕셔너리에서 2개씩 뽑아 모든 조합을 생성
        if a*2 == b*3 or a*2 == b*4 or a*3 == b*4 or b*2 == a*3 or b*2 == a*4 or b*3 == a*4:
            cnt += weights[a] * weights[b]
            
    for v in weights.values(): # 같은 무게
        if v > 1:
            cnt += sum([i for i in range(1, v)])
    return cnt
'''