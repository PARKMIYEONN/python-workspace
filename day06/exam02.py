import random
try:
    num = random.randint(0,2)
    print(f'추출된 난수 : {num}')
    result = 10/num

except Exception as e:
    print('예외발생! : ', e)
else:       #예외를 모두 피했을 때 실행될 기능을 여기에 적어줘
    print(f'10/{num} : {result}')
finally:    #예외가 있든 없든 실행해야될 기능
    print('프로그램 종료...')