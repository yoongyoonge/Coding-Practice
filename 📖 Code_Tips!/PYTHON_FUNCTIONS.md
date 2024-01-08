
### 1. ​enumerate 함수

- 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
- 인덱스와 원소를 동시에 접근할 필요가 있을 때 사용

<br>

``` python
for idx, ele in enumerate(nums)

# 출력
-> idx: 0, ele: nums[0] <br>
-> idx: 1, ele: nums[1] <br>
-> idx: 2, ele: nums[2] <br>
-> idx: 3, ele: nums[3] <br>
```

<br>

### 2. frozenset 이란?

- frozenset과 set은 모든 문법과 기능이 거의 동일
- mutable 하냐의 차이만 존재
- set은 mutable 객체이고 frozenset은 immutable 객체

<br>

### 3. set 활용법

- 저장순서를 유지하지 않고, 중복된 값의 저장을 허용하지 않는 set
- 차집합: set1 - set2
- 교집합: set1 & set2
- 합집합: set1 | set2
- 대칭 차집합((set1-set2) U (set2-set1)): set1 ^ set2

<br>

### 3. := 바다코끼리 연산자

- python 3.8에 속함
- 표현식에 이름을 부여하고 재사용할 수 있게 하는 것

``` python
li=[] 
for i in range(10):
if i==0:
    start=i 
if i==9:
    end=i 
li.append(i) 
print(li) 
print(start,end) 

#walrus operator
li = [(end:=i) if i else (start:=i) for i in range(10)]
print(li) 
print(start, end) 
```

- 단, 튜플에서 대입 연산자와 다르게 동작

``` python
x = 1, 2 # x에 (1, 2)를 대입
(x := 1, 2) # x에 1을 대입
```

<br>

### 4.zip

- 두 리스트를 묶는 함수
- 여러 iterable 객체를 하나의 tuple로 통합

``` python
name = ['merona', 'gugucon']
price = [500, 1000]

z = zip(name, price)
print(list(z))

# 출력
# [('merona', 500), ('gugucon', 1000)]

# 사용
for n, p in zip(name, price):
    print(n, p)
```

- 두 개 이상도 묶을 수 있음

``` python
for node in zip(A, B, C):
    print(node)
```

- zip함수에 *args, **kargs를 인수로 넣을 수 있음
- 이러한 *(Asterisk)가 붙은 것은 가변 인자

>*args : <br>
> 파라미터를 몇개 받을지 모르는 경우에 사용한다. <br>
> 튜플 형태로 전달된다.

> **kwargs : <br>
> 키워드를 함께 보낼 수 있다. <br>
> 딕셔너리 형태로 전달된다.

``` python
alist = [[1,2,3], [4,5,6], [7,8,9]]
for i in zip(*alist):
    print(i)

# 출력
#(1, 4, 7)
#(2, 5, 8)
#(3, 6, 9)
```

<br>

### 5. map

- map은 리스트의 요소를 지정된 함수로 처리해주는 함수
- map은 원본 리스트를 변경하지 않고 새로운 리스트를 생성

``` python
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
a
# 출력
# [1, 2, 3, 4]
# 리스트뿐만 아니라 여러 반복 가능한 객체를 넣을 수 있음
a = list(map(str, range(10)))
a
# 출력
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

<br>

### 6. defaultdict

- 딕셔너리에 접근할 때, 존재하지 않는 key에 대해 접근할 경우 keyError가 발생
- 따라서 반드시 key 값이 먼저 존재하는지 여부를 파악하고 없다면 초기화를 하여 에러 방지 필요

``` python
animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
dic = {}

for animal in animals:
    # key가 있다면 1 증가
    if animal in dic.keys():
        dic[animal] += 1
    # key가 없다면 1로 초기화
    else:
        dic[animal] = 1

print(dic)
```

- defualtdict()의 매개변수로 int를 추가하여 초기값을 0으로 세팅

``` python
from collections import defaultdict
animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
dic = defaultdict(int)

for animal in animals:
    dic[animal] += 1

print(dic)
print(dic['door'])
print(dic)
```

### ​7. remove 와 pop, del 차이

- remove는 지우고 싶은 '값'을 입력
- pop과 del은 index를 받아 지우는 것은 동일하지만 pop은 지워진 값을 반환하는 반면 del은 반환하지 않음
- pop에 아무값도 입력하지 않으면 마지막 항목을 삭제하고 돌려줍

``` python
a = [1,2,1,3,4,5,1]

#1) remove
a.remove(1)

print(a)
print(a[0])
# [2, 1, 3, 4, 5, 1]
# 2

#2) pop
removed = a.pop(1)

print(a) 
print(removed) 
print(a[0])


# [1, 1, 3, 4, 5, 1] 
# 2 
# 1


# 3) del
del a[1]

print(a) 
print(a[0])

# [1, 1, 3, 4, 5, 1] 
# 1
```

- 또한 del은 pop()과 다르게 리스트의 범위를 지정해 삭제할 수 있음

``` python
a = [1,2,1,3,4,5,1]
del a[:2]

print(a)

# [1, 3, 4, 5, 1]
```

### 8. python 의 얕은복사 vs 깊은복사

참고자료: <https://blockdmask.tistory.com/576>

- 위 참고자료 정리가 잘 되어있다..!
- 얕은복사와 깊은복사를 나누어 적용할 수 있는건 mutable한 객체들이다.
- mutable 객체와 immutable 객체의 차이는 변수를 복사했다고 생각하지만 전자는 실제로는 참조한 곳이 동일하기 때문에 같은 변수를 가르키고 후자는 값이 변경되면 무조건 참조가 변경되기 때문에 얕은 복사를 한 후 값을 변경해도 다른 객체의 값도 변경되거나 하지 않는 것에서 차이가 난다.

- 대부분의 복사는 얕은 복사이고 python 에서 깊은 복사를 하기 위해서는 copy.deepcopy를 사용해야한다.

### 9. accumulate

- import itertools
- itertools.accumulate(iterable[, func]) –> accumulate object
- 누적합을 구해주는 method, 초기값 지정이 가능
- 결과는 리스트로 반환
- <https://docs.python.org/3/library/itertools.html>

### 10. isdigit()

- 문자열이 숫자인지 판별하는 함수
- 알파벳인지 확인하는 함수는 isalpha()
- 알파벳, 숫자 모두 확인하고 싶으면 isalnum()

``` python
# Example for isdigit

ex_01 = '123'
ex_02 = '010-1234-5678'
ex_03 = "전화번호010"
ex_04 = "Phone 010"

# print result of isdigit()

print(ex_01.isdigit())
print(ex_02.isdigit()) # 기호가 포함되여 False
print(ex_03.isdigit()) # 문자가 포함되어 False
print(ex_04.isdigit()) # 공백이 포함되어 False
```

### 11. '/' vs '//'
- / 는 나눗셈 >>> 3/5 : 0.6
- // 는 몫을 구하는 연산자 >>> 10//3 : 3


### 12. find
- find는 특정 단어가 첫 번째로 나타나는 위치를 알려줌
- 해당 단어가 없다면 -1 리턴

<br>

(참고)
- rfind는 특정 단어가 마지막으로 나타나는 위치를 알려줌
- 해당 단어가 없다면 -1 리턴


### 13. sort() vs sorted()
- sort는 리스트명.sort() 형식으로 리스트형의 메소드, 원본 값을 직접 수정
- sorted는 sorted(리스트명) 형식으로 내장 함수, 원본 값은 그대로이고 정렬 값을 반환


### dict.fromkeys(seq, value)
- seq: 생성하려는 딕셔너리의 키 목록
- value: 생성하려는 딕셔너리의 값
- seq 값에 문자열을 입력할 수 도 있음

``` python
# 기본 사용법
seq = ('name', 'age', 'sex')

dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

## result ##
{'age':None, 'name':None, 'sex':None}
{'age':10, 'name':10, 'sex':10}
```

``` python
# 중복 제거 활용법, 참고 해커랭크 Merge the Tools!
# s = 'AABCAAADA'
# k = 3


divided_s = [s[i:i + k] for i in range(0, len(s), k)] # divided_s = ['AAB', 'CAA', 'ADA']

    
for val in divided_s:
    print(''.join(dict.fromkeys(val))) # AAB -> AB, 중복된 키 값은 사라짐
    #dict.fromkeys(val) = {'A': None, 'B': None}
    # ''.join(dict.fromkeys(val)) = AB

```