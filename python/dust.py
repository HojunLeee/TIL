dust = 110

if(dust > 150):
    print('매우나쁨')
elif(dust <= 150 and dust > 80):
    print('나쁨')
elif(dust <= 80 and dust > 30):
    print('보통')
else:
    print('좋음')
