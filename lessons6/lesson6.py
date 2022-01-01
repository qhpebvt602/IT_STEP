# словари
# тип dict - словари

new_dict = {}
new_list = [1,2,3]

new_dict2 = {"Notebook: " : "MSI", "Notebook: " : "Lenovo", "Owner: " : "Vlad"}
print(new_dict)
print(new_dict2)
print(new_list)



street = {"кузница" : "кузнец", "каменоломня" : "шахтер"}
print(street)
#  словари состоят из пар ключ-значение, а списки - только из элементов
man = street["кузница"]
print(man)
# с помошью [] можно обрщаться к ключам и получать знания
# кузница - кузнец
man = street["каменоломня"]
print(man)

# добавлять в словарь можно с помощью:
street["лаболатория"] = "ученый"
#
print(street)

# чтобы вывести все ключи, используем keys
print(street.keys())
# что бы вывести все значения, используем values()
print(street.values())
# чтобы вывести
print(street.items())

datebase = {"Влад": {}, "Петя": {}, "Вася": {}}
print(datebase)
