"""
题目拆分：
1. 解压缩;
2. 比较;
要意识到数字未必是一位;
"""

def decompress(input):
    result = ""
    #数字可能不止一位
    i=0
    while i<len(input):
        num=int(input[i])
        i+=1
        #注意while语法和.isdigit()方法;
        while i<len(input) and input[i].isdigit():
            num=num*10+int(input[i])
            i+=1
        result+=input[i]*num
        i+=1
    return result

def compare(input1, input2):
    return sum(1 for i in range(len(input1)) if input1[i] != input2[i])
def main():
    input1 = decompress("5555A5B")
    input2 = decompress("5554A6B")

    error=compare(input1, input2)
    print(str(error)+"\\"+str(len(input1)))

if __name__ == "__main__":
    main()