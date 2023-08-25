str = "Hello, World"
print(str, str.upper(), str.lower())    #변환된 데이터가 리턴이 될 뿐. 기존 데이터가 변하는 것은 아님.
print(str)

strList = str.split(',')
print(strList)
str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]')

str = '  !     Hello World    '
print(f'str : [{str}]')
print(f'lstrip() : [{str.lstrip(" !")}]')
print(f'rstrip() : [{str.rstrip()}]')
print(f'strip() : [{str.strip("! ")}]')

str = 'hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]')  #왼쪽과 오른쪽의 공백의 개수를 같게 만들면서. 문자열이 중앙에 배치되도록 만듦
print(f'str : [{str.center(10)}]')  #만약 짝수가 아니라면 오른쪽이 더 큼
print(f'str : [{str}]')
print(f'str : [{str.ljust(10)}]')
print(f'str : [{str.rjust(10)}]')
print(f'str : [{str.zfill(10)}]')   #앞쪽에 0으로 채워줌


str = 'Hello World!!'
print(f'"o" 위치 : {str.index("o")}') #바깥에 ''썼으니까 안쪽에 ""써줘야됨, 찾고자 하는 값이 없으면 예외 발생
print(f'"o" 위치 : {str.find("o")}')  #find는 찾고자 하는 값이 없으면 -1을 리턴
print(f'"o" 위치 : {str.rfind("o")}')  #오른쪽에서부터 왼쪽으로 가며 검색
print(f'"l"의 개수 : {str.count("l")}')
print(f'"l" => "rr"로 변환 : {str.replace("l", "rr")}')




