min=int(input("시작 숫자 입력\n"))
max=int(input("종료 숫자 입력, 0이면 무한\n"))
sx=int(min)
x=int(sx)
if min>=max:
    exit()
while max==0 or  sx<=max:
    x=int(sx)
    while not x==1:
        if(x%2==1):
                x=(3*x+1)/2
        else:
                x=x/2
    sx=sx+1
sx=sx-1
print(str(min)+"부터 "+ str(sx)+"까지의 수에서 콜라츠 추측이 성립합니다")
