dan = int(input('단을 입력하세요 : '))
i = 1

for i in range(1, 10):
    print('{0} * {1} = {2:>2}'.format(dan, i, dan * i))
    i = i + 1
