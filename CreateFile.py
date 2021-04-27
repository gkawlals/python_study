# 파일 생성하여 작성되는 내용인지 확인하기
f = open("/Users/hamjimin/data.txt",'w')
for i in range(1,11):
    data = "%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()