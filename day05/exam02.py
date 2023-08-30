def print_book(title, writer, price):
    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print(f'가격 : {price}')


print_book('홍길동전', '허균', 15000)
print()
print_book(title='홍길동전', writer='허균', price=15000)
print()
print_book(price=15000, writer='허균', title='홍길동전')

book = {'title':'홍길동전', 'writer':'허균', 'price':15000}

# dictionary는 *하나만 붙이면 key값만
# key값을 함수의 인자로 가지고 있어야만 **로 value값을 언팩킹 가능
print_book(**book)
print_book(*book)