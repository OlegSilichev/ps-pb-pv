# Программа проверки соответствия пароля политеке безопастности компании.

# Объявление переменных
password = input ('Введие пароль:') # Ввод пароля
password_mixed = False
result = 0

# Провера пароля условиям политеке безопастности компании
try:
    result = 10 / len(password) # Проверка если пароль пустой
    assert password_mixed == password.isnumeric() # Проверка если пароль только из цифр
    print ("Требования к паролю соблюдены") 
except ZeroDivisionError:
    print ("Вы ввели пустой пароль")
except AssertionError:
    print ("Ваш пароль состоит только из цифр")
except:
    print ("Какая-то неизвестная ошибка")
