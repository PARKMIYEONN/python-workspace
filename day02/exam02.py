data = [10, 40, 20, 70, 50, 60, 30, 50]

sortData = sorted(data)
maximum = sortData[-1]
minimum = sortData[0]

print(f'가장 큰 수 : {maximum}, 가장 작은 수 : {minimum}')
print(f'가장 큰 수 : {max(data)}, 가장 작은 수 : {min(data)}')
print(f'총합 : {sum(data)}')
