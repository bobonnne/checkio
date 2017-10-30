messages = input("Please write messages.")
#words= messages.split()
#print(words)

mojiretsu= "".join(messages.split())
print(mojiretsu)


secret = []
for i in mojiretsu:

    if i.isupper():
        secret.append(i)


print("".join(secret))
