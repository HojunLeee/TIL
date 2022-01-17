# 실습 문제1
# x = 10, y = 20일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오
from re import X

# 1번 방법
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y)

# 2번 방법
x, y = 10, 20
y, x = x, y
print(x, y)

num1 = 0.1 * 3
num2 = 0.3
abs(num1 - num2) <= 1e-10

a = 1
b = 2
c = 1
s = (-b +- (((b**2)-4*a*c)**0.5)) / 2*a
print(s)

n = 5
m = 9
print(('*' * n + '\n') * m)

# n = int(input())
# for i in range(1, n+1):
#     print(i)

# n = int(input())
# for i in range(n, -1, -1):
#     print(i)
s = 0
n = int(input())
for i in range(1, n+1):
    s += i
print(s)