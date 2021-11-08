import copy

a = [1, 2, 3, [1, 2, 3]]
# 赋值引用，a 和 b 都指向同一个对象
b = a
# 浅拷贝, a 和 c 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）
c = a.copy()
# 深度拷贝, a 和 d 完全拷贝了父对象及其子对象，两者是完全独立的
d = copy.deepcopy(a)

a.append(4)
a[3].append(4)

print(a)
print(b)
print(c)
print(d)
