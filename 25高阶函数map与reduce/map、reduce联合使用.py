from functools import reduce


def string2Int(str):
    # 进行reduce操作
    def fc(x, y):
        return x * 10 + y
        pass

    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]
        pass

    return reduce(fc, map(fs, str))
    pass


def main():
    str = "1943"
    # 将1943变为数字 并返回
    result = string2Int(str)
    print(result)


if __name__ == '__main__':
    main()
