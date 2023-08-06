def print_sorted_dictionary(my_dict):
    if my_dict is None:
        return
    keys = sorted(my_dict.keys())
    for key in keys:
        print("{}: {}".format(key, my_dict[key]))