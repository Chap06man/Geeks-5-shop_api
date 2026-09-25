from django.core.exceptions import ValidationError
from datetime import date

def validators_age(user):
    if not user.birthdate:
        raise ValidationError('Укажите дату рождении чтоб создать продукт')

    today = date.today()
    age = today.year - user.birthdate.year
    if (today.month,today.day) < (user.birthdate.month, user.birthdate.day):
        age -= 1
    if age < 18:
        raise ValidationError('Вам должно быть 18 чтоб создать продукт ')
    return True