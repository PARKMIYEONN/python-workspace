import  random
try:
    num = random.randint(0,2)
    print('추출된 난수 : ', num)
    data=[10,20]
    print(10/num)
    print(data[2])

except Exception as e:      # 전체 예외
    print('예외발생!!', e)


except ZeroDivisionError as e:
    print('ZeroDivisionError 예외발생!!!', e)
except IndexError as e:
    print('IndexError 예외발생!!!', e)