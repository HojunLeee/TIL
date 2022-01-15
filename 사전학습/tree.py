from re import I

# step 1 for문
# for i in range(1, 5):
#     print('*' * i)

# step 1 while문 
# i = 1
# while i <= 4:
#     print('*' * i)
#     i = i + 1

# step 2 for문
# for i in range(1, 3):
#     for k in range(1, 5):
#         print('*' * k)

# step 2 while문
# i = 1
# while i <= 2:
#     i = i + 1
#     k = 1
#     while k <= 4:
#         print('*' * k)
#         k = k + 1


# step 3
# i = 공백 k = *
i, k = 5, 1
while i >= 0:
    print('{0}{1}'.format(' ' * i, '*' * (2 * k - 1)))
    i = i - 1
    k = k + 1