print("Эта программа повторяет все что ты ей напишешь")
print()
print("Введите слово - выход, чтобы остановить программу")
print()

while True:
    print()
    user_input = input()
    if user_input == "выход":
        print("Остановка программы....")
        break
    print("Вы ввели -", user_input)
