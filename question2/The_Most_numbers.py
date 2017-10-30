num = int(input("何回入力しますか:"))
a_list = []
for i in range(num):
  print("あと{}回数値を入力してください:".format(num-i))
  a_list.append(input())
print(a_list)
a_max = max(a_list)
a_min = min(a_list)
print("最大値:",a_max)
print("最小値:",a_min)
print(int(a_max) - int(a_min))
