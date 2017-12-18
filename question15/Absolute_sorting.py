numbers_array = -1,-5,9,2,-3,4
numbers_list = []
newnum_list = []
i = 0
changenum = []
finally_list = []


numbers_list = list(numbers_array)
print("リストにした時のそのままの数" + str(numbers_list))
#print(len(numbers_list))
for i in range(len(numbers_list)):
    if numbers_list[i] < 0:
        newnum_list.append(numbers_list[i] * (-1))
        changenum.append(numbers_list[i] * (-1))
    else:
        newnum_list.append(numbers_list[i])
print("変更した数字" + str(changenum))

print("全部正にした数字" + str(newnum_list))
newnum_list.sort()
print("正にした数をソート" + str(newnum_list))

#print(len(newnum_list))
i = 0
j = 0
print("変更した個数" + str(len(changenum)))
print("入力した数字の個数" + str(len(newnum_list)))

for i in range(len(newnum_list)):
    if newnum_list[i] in changenum:
        finally_list.append(newnum_list[i] * (-1))

        print(i)
    else:
        finally_list.append(newnum_list[i])


print(finally_list)
