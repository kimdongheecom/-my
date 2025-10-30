print(1) # int

print(1.1) # float

print(1+1) # 2
print(2*2) # 4
print(3-2) # 1
print(6/2) # 3
print(2**3) # 8
print(5%3) # 2

print(type(1)) # <class 'int'>
print(type(1.1)) # <class 'float'>


print(int(1.1)) # 1
print(float(1)) # 1.0
print('1+1=',1+1) # 1+1=2
print('2*2=',2*2) # 2*2=4
print('3-2=',3-2) # 3-2=1
print('6/2=',6/2) # 6/2=3
print('2**3=',2**3) # 2**3=8
print('5%3=',5%3) # 5%3=2

print(type(int(1.1))) # <class 'int'>
print(type(float(1))) # <class 'float'>

import math
math.sqrt(16) # 4
print(math.sqrt(16)) # 4
math.pow(2,3) # 8
print(math.pow(2,3)) # 8



import random
random.randint(1,10) # 1~10 사이의 정수 중 랜덤한 수
print(random.randint(1,10)) # 1~10 사이의 정수 중 랜덤한 수
random.randrange(1,10) # 1~10 사이의 정수 중 랜덤한 수
print(random.randrange(1,10)) # 1~10 사이의 정수 중 랜덤한 수
random.choice([1,2,3,4,5,6,7,8,9,10]) # 1~10 사이의 정수 중 랜덤한 수
print(random.choice([1,2,3,4,5,6,7,8,9,10])) # 1~10 사이의 정수 중 랜덤한 수
random.shuffle([1,2,3,4,5,6,7,8,9,10]) # 1~10 사이의 정수 중 랜덤한 수
print(random.shuffle([1,2,3,4,5,6,7,8,9,10])) # 1~10 사이의 정수 중 랜덤한 수
random.sample([1,2,3,4,5,6,7,8,9,10],3) # 1~10 사이의 정수 중 랜덤한 3개의 수
print(random.sample([1,2,3,4,5,6,7,8,9,10],3)) # 1~10 사이의 정수 중 랜덤한 3개의 수


print(4//2)