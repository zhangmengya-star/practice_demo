def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('+++++++++++++++')
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1
        print('---------------')


for n in fab(5):
    print(n)
