'''
求解：
有N个手机，手机编号1-N，手机屏幕点一下变亮了，再点一下变暗了
第一次：点一下所有手机
第二次：点一下2的倍数的手机
第三下：点一下3的倍数的手机
。。。。M倍数的手机
问：最后亮着的手机
'''


def is_bright(n, m):
    if n <= 0:
        print('error')
    if m <= 1:
        print('error')

    phone_list = [0 for i in range(n)]

    j = 1
    while j <= m:
        for key, value in enumerate(phone_list):
            if (key + 1) % j == 0:
                if value == 1:
                    phone_list[key] = 0
                else:
                    phone_list[key] = 1
        j += 1

    for key, value in enumerate(phone_list):
        if value == 1:
            print(key + 1)


if __name__ == '__main__':
    is_bright(9, 3)
