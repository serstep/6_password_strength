#!/usr/local/bin/python3.5
import re, sys


def read_dict(filepath):
    with open(filepath) as dictionary :
        return dictionary.read()

def is_dict_word(password, dictionary):
    if dictionary is None:
        return False
    return True if re.search(password, dictionary, flags=re.IGNORECASE) is None else False


def is_password_valid(password):
    return True if re.search(r"[^@#$%^&*\dA-z]", password) is None else False


def get_password_strength(password, dictionary):
    password_length = len(password)
    password_rate = int(password_length >= 8) + 2 * int(password_length >= 12)
    password_rate += int(password.lower() != password and password.upper() != password)
    password_rate += 1 if not re.search(r"[\d]", password) is None else 0
    password_rate += 1 if not re.search(r"[@#$%^&*]", password) is None else 0
    password_rate += 2 if re.search(r"((19)|(20))\d\d", password) is None else 0
    password_rate += 2 * int(is_dict_word(password, dictionary))

    return password_rate


if __name__ == '__main__':
    try:
        dictionary = read_dict(sys.argv[1])
    except (FileNotFoundError, IndexError):
        dictionary = None
        print("Словарь не задан")

    password = input("Введите пароль:\n")
    if is_password_valid(password):
        print("Оценка вашего пароля:", get_password_strength(password, dictionary), "из 10")
    else:
        print("Пароль содержит запрещенные символы.")
