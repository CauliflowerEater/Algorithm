"""
题目拆分:
1. 将输入输转换为二进制String;
2. 用String.contains("101")判断是否包含101;

理论上可以优化，跳过对部分String的判断
"""

def contains101(input):
    return "101" in format(input, "b")

def main():
    n1=4
    n2=7
    result=n2-n1+1

    for i in range(n1, n2+1):
        if contains101(i):
            result-=1
    print(result)

if __name__ == "__main__":
    main()


"""
优化思路：
1. 用位运算替代替代in;
    "101" in format(input, "b")每次都会创建输入数的二进制String，后做String的contains判断;
    def contains101(x: int) -> bool:
        if x < 5:  # 二进制长度 < 3，不可能含 "101"
            return False
        L = x.bit_length()
        for i in range(L - 2):  # 子串起点（从左数第 i 位起的 3 位）
            if ((x >> (L - 1 - i)) & 1) == 1 and ((x >> (L - 2 - i)) & 1) == 0 and ((x >> (L - 3 - i)) & 1) == 1:
                return True
        return False
    通过用位运算代替String.contains判断，减少临时字符串的创建;
    
"""