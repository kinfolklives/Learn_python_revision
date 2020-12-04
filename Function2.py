def pwe_print_lol(the_list, level =1):
    for each_item in the_list:
        if isinstance(each_item, list):  # isinstance(obj, type)
            pwe_print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

fruits = [
        'apple', 2000, 
        'banana', 3000, 
        ['grape', ['mandarin', 'pear', 'lemon', 'melon']]
         ]

pwe_print_lol(fruits)
pwe_print_lol(fruits, level=0)
