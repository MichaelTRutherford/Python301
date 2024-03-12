class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Kane', 'Kalob', 'Gully']
    _list_this = "this is a private property"

the_animal = Animal()
print(the_animal.this_is_a_property['key_1'])
print(the_animal.this_list[2])

print(Animal.this_list)
print(Animal._list_this)
