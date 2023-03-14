from product_statistic import*
from phone_class_func import*
from mixin_lang_class import MixinLang


class KeyBoard(MixinLang, Item):
    pass


kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb)

print(kb.language)

kb.change_lang()
print(kb.language)

kb.language = 'CH'




# Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла
# print(len(Item.all_items))  # в файле 5 записей с данными по товарам

# item1 = Item.all_items[0]
# print(item1.item_name)

# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))

