s=0
x=int(input("원하는 숫자 입력\n"))
while not x==1:
    if x<=295147905179352825856:
        print("콜라츠 추측이 성립합니다")
        s=1
        break
    else:
        if(x%2==1):
            x=3*x+1
        else:
            x=x/2
    print(x)
if s==0:
    print("콜라츠 추측이 성립합니다")
