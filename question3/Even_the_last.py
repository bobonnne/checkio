num = int(input("何回入力しますか:"))
a_list = []
ans_list = []

for i in range(num):
  print("あと{}回数値を入力してください:".format(num-i))
  a_list.append(int(input()))
print(a_list)

a_list.sort()
#ソート後
print(a_list)

j = 0
ans = 0
for i in range(len(array)):
    if(i % 2) == 0:
         ans_list.append(a_list[i])
         j += 1
print(j)
print(ans_list)
for i in range(j):
    ans += ans_list[i]
print("偶数番目の和:",ans)
print("偶数番目の和*最後の要素:",ans * ans_list[j - 1])
