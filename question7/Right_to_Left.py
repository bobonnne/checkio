
#phrase = input("英単語をいくつか入力してください")

def left_join(phrase):
    phrases = ",".join(phrase)
    print(phrases)



    return phrases.replace("right","left")

x = left_join(("asd","right","aright"))

print(x)
