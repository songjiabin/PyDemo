#排序


def main():
    list=[23,3,1,243,4,-9,-5]

    # 默认是升序排序
    listResult =sorted(list)
    print(listResult)

    # 默认是降序序排序
    listResultReverse = sorted(list,reverse=True)
    print(listResultReverse)




    #按照绝对值 排序
    listResultAbs=sorted(list,key=abs)
    print(listResultAbs)



    #按照字符串的长短来排
    listString=["a","ab","abc","abcd"]
    listStringResult=sorted(listString,key=len)
    print(listStringResult)





if __name__ == '__main__':
    main()
