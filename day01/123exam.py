data = input('데이터 입력 : ').split()

print(type(data), data)

# for numStr in data :
#     cnt = 0
#     num = int(numStr)
#     for i in range(2, int(num)):
#         if num % i == 0:
#             cnt = cnt + 1
#     if cnt == 0:

for numStr in data:
    if numStr.isdigit():
        num = int(numStr)

num = 30
i = 2
while i < num and num % i : #순서 바뀌면 소수 판단 불가
    i += 1
print('소수' if i == num else '소수가 아님')



# for item in data:
#     print(type(item))