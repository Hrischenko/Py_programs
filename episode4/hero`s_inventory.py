# Арсенал героя
# Демонстрирует создание кортежа
# создадим пустой кортеж
# inventory = ()
# if not inventory:
#     print("Вы безоружны.")
# input("\nНажмите Eenter, чтобы продолжить.")
# теперь создадим кортеж с несколькими элементами
inventory = (
    "-меч",
    "-кольчуга",
    "-щит",
    "-целебное снадобье")
#выведем этот кортеж на экран
print("\nСодержимое кортежа:")
print(inventory)
#выведем все элменты последованоти
print("\nИтaк. в вашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Eenter, чтобы продолжить.")