'''
def check_lists(list1, list2):
    list1.sort()
    list2.sort()
    i = j = 0
    sub = sup = True
    while (sub or sup) and (i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            sub = False
            i += 1
            pass
        elif list1[i] > list2[j]:
            sup = False
            j += 1
            pass
       
        #sub = all([i in list2 for i in list1])
        #sup = all([i in list1 for i in list2])

    return sub + 2*sup
'''
