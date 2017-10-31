def index_power(array, n):
    ans = 0
    if n < len(array):
        ans = array[n] ** n
        print(ans)
    else:
        return -1

array = input("array:")
n = int(input("number:"))

y = []
for i in array.split(" "):
    y.append(int(i))

#x = list(map(int,array.split(" ")))
print(y,n)
index_power(y,n)


#index_power([1,2,3,4,5],3)
