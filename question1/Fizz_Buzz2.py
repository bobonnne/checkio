def checkio():
    num = int(input("数値を入力してください:"))
    if (num % 15) == 0:
        print("Fizz Buzz")
    elif (num % 3) == 0:
        print("Fizz")
    elif (num % 5) == 0:
        print("Buzz")
    else:
        return str()

checkio()
