# a = [1.2, 3.5, 5.4, 6.7]

# for i in range(len(a)):
#     a[i] = int(a[i])

# print(a)

# a = list(map(int,a))
# map(함수, 리스트)
# print(a)

C = input()
D = C.split()
A = D[0]
B = D[1]
print(int(A)+int(B))

A, B = map(int, input().split())
print(A+B)