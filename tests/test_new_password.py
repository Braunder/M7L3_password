import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что пароль имеет длину не менее 12 символов"""
    for length in range(1, 21): 
        assert len(generate_password(length)) == length


"""Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""

def test_diferent_password():
    """Тест что пароли отличаются"""
    for i in range(10):
        password1 = generate_password(100)
        password2 = generate_password(100)
        assert password1 != password2,"Два разных пароля"