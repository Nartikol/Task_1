try:
    file = open
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    file.close()
    print("Файл закрыт.")
    