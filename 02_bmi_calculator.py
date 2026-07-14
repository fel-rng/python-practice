def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi


def judge_bmi(bmi):
    if bmi < 18.5:
        return "低体重"
    elif 18.5 <= bmi < 25:
        return "普通体重"
    elif 25 <= bmi < 30:
        return "肥満（1度）"
    elif 30 <= bmi < 35:
        return "肥満（2度）"
    elif 35 <= bmi < 40:
        return "肥満（3度）"
    else:
        return "肥満（4度）"

    
def display_result(bmi):
    print(f"BMIは{bmi:.1f}で、判定結果は「{judge_bmi(bmi)}」です。")


def main():
    while True:
        try:
            height = float(input("身長(cm)を入力してください："))
            weight = float(input("体重(kg)を入力してください："))
        except ValueError:
            print("数値を入力してください。")
            continue
    
        if height <= 0 or weight <= 0:
            print("0より大きい数値を入力してください。")
            continue

        height_m = height / 100
    
        bmi = calc_bmi(height_m, weight)
    
        display_result(bmi)
        
        while True:
            print("もう一度計算しますか？\n")
            print("1: はい\n")
            print("2: いいえ\n")
            choice = input("選択肢を入力してください：")
            
            if choice =="1":
                break
            elif choice == "2":
                print("計算を終了します。")
                return
            else:
                print("1または2を入力してください。")
    
if __name__ == "__main__":
    main()
