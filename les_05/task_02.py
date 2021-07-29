#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# -----------------------------------------------------------------------------
#                                     Данные
import collections

hexadecs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# -----------------------------------------------------------------------------
#                                     Преобразование
def list_hex_to_dec(_lst):
    _result = []
    for _str in _lst:
        _number = 0
        for _symbol in _str:
            try:
                _d = hexadecs.index(_symbol)
            except ValueError:
                print(f'Ошибка!: {_symbol} - не является шестнадцатиричной цифрой')
                return [0, 0]
            _number = _number * 16 + _d
        _result.append(_number)
    return _result


def list_dec_to_hex(_int):
    # return [*hex(_int).split('x')[-1].upper()]
    _result = collections.deque()
    _hex = 0
    _rest = 0
    while _int > 0:
        _rest = _int % 16
        _result.appendleft(hexadecs[_rest])
        _int = int(_int / 16)
    return [*_result]


# -----------------------------------------------------------------------------
#                                     Вычисления
def calc_mul(_operands):
    a = 1
    for i in _operands:
        a *= i
    return a


# -----------------------------------------------------------------------------
#                                       Ввод
def data_input():
    inp = [[_s for _s in _h.strip()] for _h in input
    (f'Введите шестнадцатиричные числа через запятую): ')
        .upper().split(',')]
    return inp


# -----------------------------------------------------------------------------
#                                       Main
def main():
    operands = data_input()
    decs = list_hex_to_dec(operands)
    print(f'Были заданы числа: {operands}\n'
          f'Результат сложения: {list_dec_to_hex(sum(decs))}\n'
          f'Результат перемножения: {list_dec_to_hex(calc_mul(decs))}')


# -----------------------------------------------------------------------------
#                                       Вход

main()