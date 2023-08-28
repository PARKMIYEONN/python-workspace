'''
    open(파일명, 모드) # "r" "w"
    read()/write()
    close()

    with open() as 파일객체:
        read()/write()
'''

# file = open('test.txt', "w")
# file.write('hello')
# file.close()

# file = open('test.txt', 'r')
# data = file.read()
# file.close()

#close를 쓰지 않고 만드는 방식
with open('test.txt', 'r') as file:
    data = file.read()
print(f'읽어 온 데이터는 : {data}')