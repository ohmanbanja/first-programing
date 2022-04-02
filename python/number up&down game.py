import random
rn= random.randrange(1,101,1)
num=-1

t_cnt = 0 

print("1~100 숫자 up & down 게임을 시작합니다 !" )
print("______________________________________")
while(rn !=num):

    num = int(input("1~100사이의 숫자를 입력하세요 :"))

    if (num > rn):
        print("down")

    elif(num<rn):
        print("up")

    t_cnt +=1
print("___________________________________")
print(t_cnt, "번 만에 정답을 맞추셨습니다.")
    