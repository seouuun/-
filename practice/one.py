'''# 연산자
print(1 + 1) # 2
print(3 - 1) # 1
print(5 * 2) # 10
print(6 / 3) # 2

print(2 ** 3) # 2^3 = 8
print(5 % 3) # = 2 나머지 구하기
print(10 % 3) # = 1
print(5 // 3) # = 1 몫 구하기
print(10 // 3) # 3

print(10 > 3) # True 앞의 값이 뒤의 값보다 크다.
print(4 >=  7) # False 앞의 값이 뒤의 값보다 작거나 크다.
print(10 < 3) # False 앞의 값이 뒤의 값보다 작다.
print(5 <= 5) # True 앞의 값이 뒤의 값보다 작거나 같다.

print(3 == 3) # True 앞의 값과 뒤의 값이 같다.
print(4 == 2) # False 
print(3 + 4 == 7) # True

print(1 != 3) # True 앞의 값과 뒤의 값이 다르다.
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True 앞의 항과 뒤의 항이 같아야 True이다.
print((3 > 0) & (3 < 5)) # True 'and'를 쓰지 않고 '&'을 써도 된다.

print((3 > 0) or (3 < 5)) # True 'or'을 이용하면 두 항 중 하나의 항만 같아도 True가 나온다.
print((3 > 0) | (3 > 5)) # True 'or'을 쓰지 않고 '|'을 써도 된다. 

print(5 > 4 > 3) # True 연속적인 부등식도 가능하다.
print(5 > 4 > 7) # False


#간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16 'number'변수에 2를 더한것이다.
print(number)
number += 2 # 18 이것도 마찬가지로 'number'변수에 2를 더한것이다.
print(number)
number *= 2 # 36 다른 부호를 사용할수도 있다.
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 2 # 0 마찬가지로 나머지도 구할 수 있다.


# 숫자 처리 함수
print(abs(-5)) # 5 absolut, 즉 절대값이다.
print(pow(4, 2)) # 4^2 = 4*4 = 16 앞의 수를 뒤의 수만큼 제곱한다.
print(max(5, 12)) # 12 두 개의 숫자 중 더 큰 값을 출력한다.
print(min(5, 12)) # 5 두 개의 숫자 중 더 작은 값을 출력한다.
print(round(3.14)) # 3 반올림이다.
print(round(4.99)) # 5 반올림이다.

from math import * # 나중에 배울 내용이다. 'math'라이브러리 안에 있는 모든 것을 이용하겠다는 것이다.
print(floor(4.99)) # 4 내림.
print(ceil(3.14)) # 4 올림.
print(sqrt(16)) # 4 제곱근.


#랜덤함수(난수)
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성.
print(random() *  10) # 0.0 ~ 10.0 미만의 임의의 값 생성.
print (int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성


print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성.

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성.

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성.'''


# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함.
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함.
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제) 
#모프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")