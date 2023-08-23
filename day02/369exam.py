

# while num:
#     if num % 10 in (3, 6, 9):
#         cnt += 1
#     num //= 10
# print(cnt)

for i in range(1, 260):
    num = i
    cnt = 0
    n10 = i // 10
    while num:
        if num % 10 in (3, 6, 9):
            cnt += 1
        num //= 10
    print('짝'*cnt if cnt else i, end='')
    print('' if i % 10 else '뽀' * n10, end='')
    print('' if i % 10 else '숑')