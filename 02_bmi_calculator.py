def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

    
def display_result(bmi):
    print(f"BMIは{bmi:.1f}です。")


def main():
    height, weight = map(float, input("身長(cm)と体重(kg)を入力してください（例：170 60）：").split())
    height_m = height / 100
    
    bmi = calc_bmi(height_m, weight)
    
    display_result(bmi)
    
if __name__ == "__main__":
    main()