def no_c(my_string):
    my_new_string = my_string.translate({ord("c"): None, ord("C"): None})
    return my_new_string




print(no_c("Hoxclbecrton SChool"))
