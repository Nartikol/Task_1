print("Добро пожаловать в калькулятор")

def summa (num1, num2):
    return num1 + num2


def sub (num1, num2):
    return num1 - num2


def mult (num1, num2):
    return num1 * num2


def div (num1, num2):
    return num1 / num2


def calc(num1, num2, oper):
    result = None

    if oper == '+':
        result = summa(num1, num2)

    elif oper == '-':
        result = sub(num1, num2)

    elif oper == '*':
        result = mult(num1, num2)

    elif oper == '/':
        if (num2 == 0):
            print('Деление на ноль запрещено!')

            return

        result = div(num1, num2)

    elif oper == '%':
        result = num1 / num2 * 100

    elif oper == '**':
        result = num1 ** num2

    else:
        print('Некорректная операция!')

    return result


def operation():
    mes = input('Выберите операцию (Введите +, -, *, /, %, **):\n '

                '+ - сложение двух чисел\n'

                '- - вычитание двух чисел\n'

                '* - умножение двух чисел\n'

                '/ - деление двух чисел\n'

                '% - процент первого числа от второго\n'

                '** - возведение первого числа в степень второго\n')

    if mes == '+':
        print('Вы выбрали сумму')

    elif mes == '-':
        print('Вы выбрали разность')

    elif mes == '*':
        print('Вы выбрали умножение')

    elif mes == '/':
        print('Вы выбрали деление')

    elif mes == '%':
        print('Вы выбрали нахождение процента первого числа от второго')

    elif mes == '**':
        print('Вы выбрали возведение в степень')


    correct_operations = ['+', '-', '*', '/', '%', '**']

    while mes not in correct_operations:
        print('Такой операции нет в списке. Попробуйте ещё!')

        mes = input()

    return mes


def run():
    try:
        num1 = float(input('Укажите первое число: '))
        num2 = float(input('Укажите второе число: '))

        op = operation()

        result = calc(num1, num2, op)

        print('{} {} {} = '.format(num1, op, num2))
        print(f'Результат: {result}')

    except ValueError:
        print("Ошибка: введено не число!")


progam_is_running = True

while(progam_is_running):

    run()
    answer = input('Желаете продолжить?\n'

      ' Введите + если да и прочий символ, если нет: ')

    if answer != '+':

        progam_is_running = False
