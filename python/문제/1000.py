# a = [1.2, 3.5, 5.4, 6.7]

# for i in range(len(a)):
#     a[i] = int(a[i])

# print(a)

# a = list(map(int,a))
# map(함수, 리스트) -> 리스트에 함수를 전부 적용하는 함수
# print(a)

# 1000 - 1
# split : 문자열을 일정한 규칙으로 잘라서 나눠줌
C = input()
D = C.split()
A = D[0]
B = D[1]
print(int(A)+int(B))

# 1000 - 2
A, B = map(int, input().split())
print(A+B)
