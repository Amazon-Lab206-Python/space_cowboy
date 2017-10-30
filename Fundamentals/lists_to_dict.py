def making_dictionaires(list1, list2):
    the_dict = {}
    for i in range(0, len(list1)):
        the_dict[list1[i]] = list2[i]
    return the_dict