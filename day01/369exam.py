import random

r = random.randint(20,60)
print(r)



for i in range(r):
    bbo = (i+1) // 10
    jja = (i+1) % 10
    if (i+1) % 10 == 0:
        if bbo == 3 or bbo == 6 or bbo == 9:
            print('짝',bbo * '뽀', '숑', sep='')
        else:
            print(bbo * '뽀', '숑', sep='')
    elif bbo == 3 or bbo == 6 or bbo == 9:
        if jja == 3 or jja == 6 or jja == 9:
            print('짝짝')
        else:
            print('짝')
    elif jja == 3 or jja == 6 or jja == 9:
            print('짝')
    else:
        print(i + 1)
