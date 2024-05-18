x=int(input("원하는 숫자 입력"))
while not x==1:
    if(x%2==1):
            x=3*x+1
    else:
            x=x/2
    print(x)
print("콜라츠 추측이 성립합니다")
