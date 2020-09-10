print('간단한 설문조사를 진행하겠습니다.')

name = input('1. 당신의 이름은 무엇인가요?')
number = input('2. 당신의 학번은 무엇인가요?')
major = input('3. 당신의 전공은 무엇인가요?')
place = input('4. 입학 후 학교에서 가장 먼저 방문한 곳은 어디인가요?')
event = input('5. 학교 생활 중 가장 기대하는 것은 무엇인가요?')



print('=====')
print('%s 님 안녕하세요.'%(name))
print('%s 님의 전공은 %s 이며, 학번은 %s 입니다.'%(name, major, number))
print('%s 님은 한국외국어대학교에서 %s 에 가장 먼저 방문하셨습니다.'%(name, place))
print("%s 을(를) 가장 기대하는 %s 님의 학교 생활을 응원합니다."%(event, name))
print('=====')