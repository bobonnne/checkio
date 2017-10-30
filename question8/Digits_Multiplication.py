x = input("数字を羅列してください")
x_list = list(x)

num = len(x_list)


ans =1
for i in range(num):
        if int(x_list[i]) == 0:
            ans = ans * 1
        else:
            ans = ans * int(x_list[i])
print(ans)
