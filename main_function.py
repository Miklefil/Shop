from product_statistic import*
from phone_class_func import*

phone1 = Phone("iPhone 14", 120_000, 5, 2)

print(phone1)
print(repr(phone1))
phone1.number_of_sim = 0


# Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла
# print(len(Item.all_items))  # в файле 5 записей с данными по товарам

# item1 = Item.all_items[0]
# print(item1.item_name)

# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))

