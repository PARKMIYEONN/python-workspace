
# 문자열을 입력받아 모음을 제것하고 출력

data = input('문장을 입력하세요 : ')

# data2 = [s for s in data if s not in 'aeiouAEIOU .']
data2 = [s for s in data if s.isalpha() and s not in 'aeiouAEIOU']
print(''.join(data2))