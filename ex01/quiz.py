import random

def shutudai():
    q1 = ["サザエの旦那の名前は？", "マスオ", "ますお"]
    q2 = ["カツオの妹の名前は？", "ワカメ", "わかめ"]
    q3 = ["タラオはカツオから見てどんな関係？", "甥", "おい", "甥っ子", "おいっこ"]
    num = random.randint(1, 3)
    if num == 1:
        print(q1[0])
    if num == 2:
        print(q2[0])
    if num == 3:
        print(q3[0])
    return num

def kaito(num):
    q1 = ["サザエの旦那の名前は？", "マスオ", "ますお"]
    q2 = ["カツオの妹の名前は？", "ワカメ", "わかめ"]
    q3 = ["タラオはカツオから見てどんな関係？", "甥", "おい", "甥っ子", "おいっこ"]
    ans = input("なんだろう…？")
    if num == 1:
        if ans == q1[1] or q1[2]:
            print("…正解のようだ")
        else:
            print("反応がない…違うみたいだ…")
    if num == 2:
        if ans == q2[1] or q2[2]:
            print("…正解のようだ")
        else:
            print("反応がない…違うみたいだ…")
    if num == 3:
        if ans == q3[1] or q3[2] or q3[3] or q3[4]:
            print("…正解のようだ")
        else:
            print("反応がない…違うみたいだ…")

num = shutudai()
kaito(num)