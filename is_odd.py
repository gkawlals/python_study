a = int(input("숫자를 입력해보아요 홀짝을 알아봐"))
def is_odd (a):
    if a%2 == 0:
        print("찍수입니다.")
    else :
        print("홀수입니다.")

print(is_odd(a))