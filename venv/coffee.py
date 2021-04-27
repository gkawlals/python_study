coffee = 10
while True:
    money = int(input("돈을 넣어주세요 :"))
    if money == 300:
        print("커피를준다")
        coffee = coffee - 1
    elif money > 300 :
        print("남은돈 %d원을 주며 커피를 준다." % (money - 300))
        coffee = coffee -1
    else :
        print("돈없으면 커피 없어요")
        print("남은 커피는 %d잔 입니다." % coffee)
    if coffee == 0:
        print("SOLD OUT CLOSE THE HERE")
        break