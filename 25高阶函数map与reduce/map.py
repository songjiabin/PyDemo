# 将传入的函数依次作用在序列中的每一个元素，
# 并把结果作为新的Iterator返回

# 将传入的char 变为 int 类型
def charToint(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]


def main():
    result = charToint("4")
    print(result)


    #也可以使用map
    res=map(charToint,["0","5"])
    #返回的res是一个Iterator的对象
    print(list(res))














if __name__ == '__main__':
    main()
