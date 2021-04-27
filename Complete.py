marks = [90, 80, 25, 61, 29, 56]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d 학생은 합격! " % (number + 1))
