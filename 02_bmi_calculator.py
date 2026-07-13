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
    height, weight = map(float, input("身長(cm)と体重(kg)を入力してください（例：170 60）：").split())
    height_m = height / 100
    
    bmi = calc_bmi(height_m, weight)
    
    display_result(bmi)
    
if __name__ == "__main__":
    main()