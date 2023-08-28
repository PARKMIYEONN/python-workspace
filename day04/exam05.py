# quit가 나올때까지 문자열을 입력받아 test02.txt에 저장
# test02.txt에 저장된 모든 문자열을 읽어서 모니터에 출력

with open('text02.txt', 'w') as file:
    print('문자열을 입력하세요. quit 입력시 종료')
    while True:
        msg = input()
        if msg == 'quit':
            break
        file.write(f'{msg}\n')              #줄 바꾸는 방법 1
        # file.write('{0}\n'.format(msg))   #줄 바꾸는 방법 2

print('파일 저장 완료...')

print('< 읽어온 데이터 >')

with open('text02.txt', 'r') as file:
    # for i in range(3):
    #     msg = file.read()
    #     print(msg)

    lines = file.readlines()

print('< 읽어온 데이터 출력 >') #print 자체에 end 속성이 들어있어서 디폴트인 엔터가 자동으로 들어감. 우리가 적어준 엔터까지 두 칸이 띄워짐
for line in lines:
    print(line.rstrip('\n'))

# readline 사용해보기
with open('text02.txt', 'r') as file:
    line = file.readline()
    print('[{}]'.format(line.rstrip('\n')))

    line = file.readline()
    print('[{}]'.format(line.rstrip('\n')))

    line = file.readline()
    print('[{}]'.format(line.rstrip('\n')))


# 방법 1
with open('text02.txt', 'r') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        print('방법1 : ' + line.strip('\n'))


print()

# 방법 2
with open('text02.txt', 'r') as file:
    line = file.readline().rstrip('\n')
    while line != '':
        print('방법2 : ' + line)
        line = file.readline().rstrip('\n')

print()

# 방법 3
with open('text02.txt', 'r') as file:
    for line in file:
        print('방법3 : ' + line.rstrip('\n'))





