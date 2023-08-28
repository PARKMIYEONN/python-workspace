data = [10, 20, 30, 40]

print(data)
print(*data)    #== (*[10, 20, 30, 40])    #== print(10, 20, 30, 40) 원소들의 집합이라는 형태로 바꿔주라는 의미

def getTotal(a, b, c, d):
    return a+b+c+d

# def getSum(nums):
#     s = 0
#     for n in nums:
#         s += n
#     return s

def getSum(*nums):
    # print(nums, type(nums))
    s = 0
    for n in nums:
        s += n
    return s

print(f'총합 : {getTotal(1,2,3,4)}')
print(f'총합 : {getTotal(10,20,5,6)}')
print(f'총합 : {getTotal(*data)}')
print(f'총합 : {getTotal(*[10, 20, 30, 40])}')

# print(getSum([10, 20, 30, 40]))
print(getSum(10, 20, 30, 40))
print(getSum(10, 20, 30, 40, 50, 60))
print(getSum(10, 20))
