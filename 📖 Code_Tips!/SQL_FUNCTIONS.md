## ​[제어 흐름 함수]

#### 1. IF(수식, 참 값, 거짓 값)

- 수식 = 참 -> 참 값
- 수식 = 거짓 -> 거짓 값

#### 2. IFNILL(수식1, 수식2)

- 수식1 = NULL -> 수식2 값
- 수식1 = NOT NULL -> 수식1 값

#### 3. NULLIF(수식1, 수식2)

- 수식1 != 수식2 -> 수식1 값
- 수식1 = 수식2 -> NULL

#### 4. CASE ~ WHEN ~ ELSE ~ END

- CASE값 = WHEN값 -> THEN 값
- CASE값 != WHEN값 -> ELSE 값

<br>

## [문자열 함수]

#### 1. ASCII, CHAR

- ASCII: 아스키 코드값 -> 문자
- CHAR: 문자 -> 아스키 코드값

#### 2. BIT_LENGTH, CHAR_LENGTH, LENGTH

- BIT_LENGTH: 할당된 BIT 크기
- CHAR_LENGTH: 문자수
- LENGHT: 할당된 BYTE 수

#### 3. CONCAT, CONCAT_WS

- CONCAT(A, B): A, B 문자 연결
- CONCAT_WS(구분자, A, B): A와 B 사이에 구분자 추가되어 문자 연결

#### 4. ELT, FIELD FIND_IN_SET, INSTR, LOCATE

##### 1) ELT (위치, 문자1, 문자2, 문자3, ...): 위치 X 번째에 해당하는 문자열 반환

##### 2) FIELD (찾는 문자, 문자1, 문자2, 문자3, ...)

- 문자 목록 중 찾는 문자의 위치 X 반환
- 매치되는 문자 없으면 0 반환

##### 3) FIND_IN_SET (찾는 문자, 문자열 리스트)

- 문자열 리스트에서 찾는 문자의 위치 X 반환
- 문자열 리스트는 '콤마(,)'로 구분되며, 공백이 없어야 함. ('문자1, 문자2, 문자3')

##### 4) INSTR (문자열 리스트, 일부 문자열)

- 문자열 리스트 중 일부 문자열 시작 위치 X 반환
- 문자열 리스트의 '콤마(,)'는 하나의 문자로 인식됨. (FIN_IN_SET과 차이점)

##### 5) LOCATE(일부 무자열, 문자열 리스트)

- INSTR과 동일하나, 파라미터 순서가 반대
- 문자열 리스트 중 일부 문자열의 시작 위치 X 반환

#### 5. FORMAT

- 1000단위 콤마(,) 추가 + 소숫점 자릿수 지정

#### 6. BIN & HEX & OCT

- 2진수, 16진수, 8진수 값

#### 7. INSERT (기존 문자열, 대체시작 위치, 삭제 길이, 삽입 문자열)

- '기존 문자열'에서 '대체 시작위치'부터 '삭제 길이' 만큼 삭제한 후, '삽입 문자열'을 추가함

#### 8. LEFT & RIGHT (문자열, 길이)

- '문자열' 왼쪽 또는 오른쪽에서 '길이'만큼 반환

#### 9. UPPER & LOWER (문자열)

- 대문자 또는 소문자로 변환

#### 10. LPAD & RPAD (문자열, 길이, 추가 문자)

- '문자열'을 '길이'만큼 늘린 후 오른쪽 또는 왼쪽에 '추가 문자'를 합쳐서 반화

#### 11. LTRIM & RTRIM & TRIM (문자열)

- 왼쪽, 오른쪽, 양쪽의 공백을 제거 (중간 공백은 제외)

##### 11-1 TRIM(LEADING/BOTH/TRAILING 삭제할 문자 FROM 문자열)
  - 문자열의 앞, 뒤, 양쪽에 있는 '삭제 문자'를 삭제

#### 12. REPEAT (문자, 반복 횟수)

- '반복횟수'만큼 반복한 값을 반환

#### 13. REPLACE (문자열, '삭제할 문자', '대체할 문자')

- '문자열'안에서 '삭제할 문자'를 없애고, 그 자리에 '대체할 문자'를 넣어 반환

#### 14. REVERSE (문자열)

- 문자열을 끝부터 반대호 반환

#### 15. SPACE (10)

- '숫자'만큼 공백을 반환

#### 16. SUBSTRING(문자열, 시작위치, 길이)

- '문자열'에서 '시작위치'부터 '길이' 만큼만 반환

#### 17. SUBSTRING_INDEX (문자열, 구분자, 횟수)

- 횟수 = 양수 -> '문자열' 왼쪽부터 '횟수'만큼 반환하고, 이후는 삭제
- 획수 = 음수 -> '문자열' 오른쪽부터 '횟수'만큼 반환하고, 이후는 삭제

<br>

## [수학 함수]

#### 1. ABS (숫자)

- 숫자의 절대 값을 반환

#### 2. CEILING, FLOOR, ROUND (숫자)

- 숫자가 소수점일 때, 올림, 내림, 반올림을 반환

#### 3. CONV(숫자, 원래 진수, 변환할 진수)

- 진수 변환

#### 4. DEGREES, RADIANS, PI

- DEGRESS: 라디안 값 -> 각도 값으로 변환
- RADIANS: 각도 값 -> 라디안 값으로 변환
- PI: 파이값 반환ㄴ

#### 5. MOD (숫자1, 숫자2)

- 숫자1을 숫자2로 나눈 후 나머지 값을 반환
- 숫자1%숫자%로 표현할 수 있음

#### 6. POW, SQRT

- POW (숫자1, 숫자2): 숫자1을 숫자2만큼 제곱한 값 반환
- SQRT(숫자): 해당 숫자의 루트값 반환

#### 7. SIGN(숫자)

- 숫자의 양수, 음수 여부를 반환
- 1 (양수) / 0 / -1 (음수)

#### 8. TRUNCATE (숫자, 정수)

- 숫자를 '정수'위치까지 반환하고, 나머지는 버림
- 정수 = 양수: 숫자의 소수점 어느 자리까지 표시할 지
- 정수 = 음수: 숫자의 정수 어느 자리까지 표시할 지

<br>

## [날짜, 시간 함수]

#### 1. ADDDATE, SUBDATE (날짜, 더하거나 뺄 일수)

#### 2. ADDTIME, SUBTIME (시간, 더하거나 뺄 시간)

#### 3. CURDATE, CURTIME, NOW, SYSDATE()

- CURDATE / CURRENT_DATE: 현재 연-월-일
- CURTIME / CURRENT_TIME: 현재 시:분:초
- NOW / SYSDATE / LOCALTIME / LOCALTIMESTAMP: 현재 연-월-일 & 시:분:초

#### 4. YEAR, MONTH, DAY, DAYOFMONTH (날짜) / HOUR, MINUTE, SECOND (시간)

- 연, 월, 일, 시, 분, 초 구하기

#### 5. DATE(날짜), TIME(시간)

- DATE: 연-월-일 반환
- TIME: 시:분:초 반환

#### 6. DATEDIFF(날짜1, 날짜2), TIMEDIFF (시간1, 시간2)

- DATEDIFF: [날짜1] - [날짜2]의 결과 반환
- TIMEDIRR: [시간1] - [시간2]의 결과 반환

#### 7. DATEOFWEEK, MONTHNAME, DAYOFYEAR (날짜)

- DATEOFWEEK: 요일값 반환 (1: 일요일, 2: 월요일 ~ 7: 토요일)
- MONTHNAME: 해당 월 이름 반환 (SEPTEMBER, OCTOBER)
- DAYOFYEAR: 1년 365일 중 오늘에 해당하는 일수 반환

#### 8. LAST_DAY (날짜)

- 날짜가 속한 달의 마지막 일 반환

#### 9. MAKEDATE (연도, 정수)

- 주어진 주어진 시, 분, 초를 이용해서 TIME 형식 (시:분:초)로 변환

#### 10. PERIOD_ADD(연월, 개월수), PERIOD_DIFF(연월1, 연월2)

- PERIOD_ADD: 연월에서 개월수만큼 지난 연월을 반환
- PERIOD_DIFF: [연월1 - 연월2] 값 반환
- 연월은 'yyyyMM'형식으로 작성 필요

#### 11. QUARTER (날짜)

- 날짜가 속한 분기를 반환

#### 12. TIME_TO_SEC (시간)

- 해당 시간을 초로 반환

<br>

## [시스템 정보 함수]

#### 1. USER, DATABASE ()

- 현재 사용 중인 유저, 데이터베이스 조회

#### 2. FOUND_ROWS ()

- 바로 앞 SELECT 문에서 조회된 행의 개수 반환

#### 3. ROW_COUNT ()

- INSERT, UPDATE, DELETE 문: 수정, 삭제, 입력된 행의 개수 반환
- CREATE, DROP 문 = 0 반환
- SELECT 문: -1 반환

#### 4. VERSION ()

- 현재 MySQL 버전 확인

#### 5. SLEEP (초)

- x초 후에 결과값이 반환

<br>
<br>

#### 참고

- <https://anotherspringfield.tistory.com/95>
- <https://anotherspringfield.tistory.com/97>
