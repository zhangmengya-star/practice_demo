# 字符串中只有字符'('和')'。合法字符串需要括号可以配对
# 例如 输入："()",输出：true

def is_valid(s: str):
    s_len = len(s)
    if s_len == 0 or s_len % 2 != 0:
        return False

    stack = []
    for i in s:
        if i == '(':
            # 进栈
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                # 出栈
                stack.pop()
    if len(stack) != 0:
        return False
    return True

if __name__ == '__main__':
    str1 = "()"
    str2 = "(()))"
    str3 = "()()("
    str4 = "))(("
    str5 = ""
    str6 = "(())"
    print(is_valid(str1))
    print(is_valid(str2))
    print(is_valid(str3))
    print(is_valid(str4))
    print(is_valid(str5))
    print(is_valid(str6))
