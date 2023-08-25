
print('hello python')

my_string = 'He11oWor1d'
overwrite_string = 'lloWorl'
s = 2

my_string1 = my_string[s+len(overwrite_string):]
print(my_string1)


my_string2 = my_string[:s]
print(my_string2 + overwrite_string + my_string1)


array = [1, 1, 2, 2]

maxArr = max(array)
cntArr = [0] * (maxArr+1)
print(cntArr)

for i in range(0,len(array)):
    cntArr[array[i]] += 1

maxCountIndex = cntArr.index(max(cntArr))

modes = []
for i in range(len(cntArr)):
    if cntArr[i] == max(cntArr):
        modes.append(i)

if len(modes) == 1:
    result = modes[0]
else:
    result = -1

print(result)

print(cntArr)

print(array[max(cntArr)+1])


