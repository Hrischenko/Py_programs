#Арсенал героя 3.0
# Демонстрирует работу со списками
# создадим список с несколькими элементами и выведем его с помощью цикла for

inventory = ["-меч", "-кольчуга", "-щит", "-целебное снадобье"]
print("\nСодержимое списка:")
for item in inventory:
    print(item)
print(inventory)
#выведем все элменты последованоти
print("\nСейчас в вашем распоряжении", len(inventory), "предметов")
input("\nНажмите Eenter, чтобы продолжить.")