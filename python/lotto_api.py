# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json() # url에 조회요청해서(get) 응답받은 결과를(response) json함수를 통해 파이썬 문법에 맞게 변환
# 요청 보내서 응답 받은 문서를 출력

print(response)
# 당첨번호 정보를 리스트에 담아보자
winners = []
# 1~7까지 반복
for num in range(1,7):
    print(response[f'drwtNo{num}'])
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)

# print(response['drwtNo6'])
# print(response['drwtNo5'])
# print(response['drwtNo4'])
# print(response['drwtNo3'])
# print(response['drwtNo2'])
# print(response['drwtNo1'])