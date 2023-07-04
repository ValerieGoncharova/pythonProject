def numeral_count(num):
    if num < 0:
        num = 0
    return len(str(num))

N = int(input("Введите кол-во задач: "))

max_digits = 0
task_number = 0

for i in range(N):
    num = int(input("Введите число: "))
    digits = numeral_count(num)
    if digits > max_digits:
        max_digits = digits
        task_number = i + 1

print("Первая задача на обработку:", task_number)