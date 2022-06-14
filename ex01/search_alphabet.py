import random
import time

max_question_num = 10
target_num = 7 # 対象文字数
miss_num = 2   # 欠損文字数

def main():
    start_time = time.time() # 時間の計測を開始する
    for i in range(max_question_num):
        ans = search_alphabet()
        check = response(ans)
        if check == 1:
            break
    end_time = time.time() # 時間の計測を終了する
    elapsed_time = end_time - start_time # 経過時間の計算

def search_alphabet():
    miss_alphabet = []
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    all_alphabet = random.sample(alphabet, target_num)
    print(f"対象文字：{all_alphabet}")

    for i in range(miss_num):
        pop_num = random.randint(0, len(all_alphabet))
        miss_alphabet.append(all_alphabet.pop(pop_num))
    print(f"表示文字：{all_alphabet}")

def response(ans):
    response_num = int(input("欠損文字数を答えてください。"))
    if response_num == miss_num:
        print("あたりです。では欠損文字を1つずつ答えてください。")
        response_split(ans)
    else:
        print("…違います。")
        return 0
main()

def response_split(ans):
    for i in range(miss_num):
        response_alphabet = input(f"{i+1}つ目の文字を答えてください。")
        if response_alphabet not in ans:
            print("…違います。最初からやり直してください。")
            print("-----------------------------------------------")
            return 0
        ans.remove(response_alphabet)
    return 1