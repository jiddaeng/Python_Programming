#반복문 : while문, for문

#while문
#1 ~ 10까지의 반복 출력
i = 1
while i <= 10 : 
    print(i)
    i+=1
else :
    print("end")

nums = [1,3,5,7,9]
target = 2
i = 0
while i < 5 :
    if nums[i] == target :
        break
    i += 1

else :
    print("없음")



# 1~ 10까지의 합
i = 1
tot = 0

while i <= 10 :
    if i % 2 == 0:
        tot += i
    i += 1
else :
    print(tot)
