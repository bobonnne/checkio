words = input("空白で区切られたワードと数をもつ文字列を入力してください")
#words1 = "asd sdf dfg"
#words2 = "1 2 3 4 5"
#words3 = "asd 2 sdf dfg ghj"

def checkio(words):
    x = words.split(" ")
    print(x)

    #ans = []
    j = 0
    flag = False

    for i in x:
        """
        if i == x[-1]:
            return False
        """
        if not i.isdigit():
            #ans.append(i)
            j += 1
            if j == 3:
                return True
                #flag = True

        else:
            j = 0

    """
    if flag == True:
        return True
    else:
        return False
    """
    return False

print(checkio(words))
