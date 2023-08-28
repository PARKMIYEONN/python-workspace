'''
    input.txt 읽어 다음의 결과를 출력하시오
    1. 총 단어의 개수 세어보기
    2. 단어의 비도수 세어보기 ( 알파벳 순으로 출력 )
        a       15
        avove   1
        ...
    3. 단어가 몇번째 라인에 나왔는지 출력
        a 15 2,3,5, ...
'''

with open('input.txt', 'r') as file:
    for line in file:
        print(line.rstrip('\n'))

