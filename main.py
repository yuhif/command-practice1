import calc_bmi

h = int(input("身長："))
w = int(input("体重："))

print(f"bmiは{calc_bmi.get_bmi(h, w)}です。")
