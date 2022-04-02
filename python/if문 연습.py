#weather = input('오늘 날씨 어떨까?')
#if weather == '비'  or weather =='눈':
 #   print('우산을 챙기세요')
#elif weather == '미세먼지':
#    print('마스크를 챙기세요')
#else:
#    print('준비물이 필요 없어요')
   
#samanda = input("오늘 날씨 좋지?")
#if samanda == ("응") or  ("그렇게") or ("아니"):
#    samanda1 = input("그래? 그렇구나. 기분은 좀 어떄?")
#if samanda1 == ("별루"):
#    samanda1 = input("그건좀 슬프네")

temp = int(input('기온은 어떄요'))
if temp > 30:
    print('물 챙겨가세요')
elif temp <30 and temp >10:
    print('날씨가 적당히 좋네요')

elif temp < 10 and temp > 0:
    print('추워요 외투챙기세요')
else:
    print('절 대 나가지마')
