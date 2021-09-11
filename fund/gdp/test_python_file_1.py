class variable:
    x = 1
    y = 'a'
    z = True

dd = variable()
print(hasattr(dd, 'x')) # 返回 True
print(hasattr(dd, 'y')) # 返回 True
print(hasattr(dd, 'z')) # 返回 True
print(hasattr(dd, 'no')) # 返回 False