list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
    new_items = type(items)
    return new_items

new_list = list(map(type_list, list_Strings))
print(new_list)