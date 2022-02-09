# def add(x, y):
#     print(x)
#     print(y)
# # add(2, x=5)
# add(y=5, x=2)
# add(2, y=5)
# keyword가 먼저 나오면 뒤에 위치가 박살난다!
# 위치인자가 먼저 나오면 상관없음! 하지만 한곳에 중복해서 들어가면 안된다!

# 몇개의 값이 들어올지 예측할 수 없고 다수의 값을 받을 수 있는 상태
# def add(*args, a):
#     return args, a
# print(add(1,2,3,4, a=6))

# def another_add(a, *args):
#     return a, args
# print(another_add(1,2,3,4,5))

# 정의할 수 없음 why? a=1로 지정해버려도 kwargs 가 빨아먹기 때문 (dict로)
# def add(**kwargs, a):

# def add(a, **kwargs):
#     return a, kwargs
# print(add(a=1, b=2, c=3, d=4))

# **kwargs는 항상 맨뒤에 적어라!!

# scope
## lifecycle이 존재
# global_a = 1
# def enclosed():
#     a = 20

#     def local():
#         a = 300
#         print(a)
#     local()
#     print(a)

# enclosed()
# print(global_a)

# global_a = 1
# def enclosed(a):
#     a = 20

#     print(a)
#     return a

# a = enclosed()
# print(global_a)


# nums = [1, 2, 3, 4]

# def new():
#     nums[0] = 100

# new()
# print(nums)

# map 활용
# input_value = input()
# print(type(input_value))
# 입력받은 변수를 n,m으로 나눠서 저장
# input_value.split()
# print(type(input_value))

a = input().split()
print(a)
n,m = map(int, a)
print(list(map(int,a)))
print(n,m)
# map(각 요소에 적용하고 싶은 함수의 이름, 적용할 객체)

# filter
# filter(각 요소에 적용하고 싶은 함수, 객체) -> true값만 모아줌


# zip
# 튜플로 묶어줌

# lambda
# 익명함수

# 재귀함수
def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n-1)

f(4)