# 1 ~ 45 중 6개만 뽑아서 리스트에 출력
# random.sample : 리스트에서 특정 수의 요소를 임의적으로 "비복원추출" 
# ex) random.sample(numbers,6)


# random 불러오기
import random
# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json() # url에 조회요청해서(get) 응답받은 결과를(response) json함수를 통해 파이썬 문법에 맞게 변환
# 요청 보내서 응답 받은 문서를 출력

# print(response)
# 당첨번호 정보를 리스트에 담아보자
winners = []
# 1~7까지 반복
for num in range(1,7):
    # print(response[f'drwtNo{num}'])
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)
# 1 ~ 45의 숫자 범위 만들기
# range(start, end, step)
numbers = list(range(1, 46))
# 비복원추출로 6개 뽑기
# 6개 뽑아서 lotto 변수에 담기를 1000번 반복
for i in range(10):
    lotto = random.sample(numbers, 6)
    # 당첨 횟수를 기록
    count = 0
    # print(lotto[0] ~ [5])
    for num in lotto:
        # print(num)
        # lotto가 가지고 있는 값들 하나하나가
        # winners 안에 들어 있다면
        # 한개 당첨
        if num in winners:
            count = count + 1
        # 당첨 횟수를 기록
        # 6개 당첨 == 1등
    if count == 6:
        print(i)
        print('1등!!!!!!') 
