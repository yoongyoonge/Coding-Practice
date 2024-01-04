# 이진 탐색이란 ?

오름차순으로 정렬된 배열에서 원하는 숫자(target)을 찾는 알고리즘입니다.

기본 풀이 방법
1. 배열 전체의 중간값을 target 값과 비교
2. 중간값이 target 값보다 크면 왼쪽 부분만 선택
3. 왼쪽부분의 중간값을 다시 target 과 비교



정방향으로 푸는 방법과 재귀로 푸는 방법 두 가지가 있습니다. <br>
정방향도 어떻게 보면 개념적으로는 재귀로 푸는 방법과 같은 방법입니다.

## source code

### 정방향

``` python 
target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1
```


### 재귀(Recursive)
``` python 
def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else: 
        return False

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

binarySearch(m_list,target,0,right)
```


참고: https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC