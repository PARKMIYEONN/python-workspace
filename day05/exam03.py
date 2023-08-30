def print_book_info(**args):    #dictionary의 팩킹 방식을 사용해야 함. 가변인수를 사용할 때. 인자의 개수를 정해주지 않았을 때
    for key, value in args.items():
        print(f'{key} : {value}')
    print('=' * 20)

print_book_info(title='홍길동전', writer='허균', price=15000)
print_book_info(title='홍길동전', writer='허균')
print_book_info(title='홍길동전')
print_book_info(title='홍길동전', price=15000)

print()
book = {'title':'홍길동전', 'writer':'허균', 'price':15000}
print_book_info(**book)