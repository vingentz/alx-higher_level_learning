#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nList = []
    for k in range(list_length):
        division = 0
        try:
            division = my_list_1[k] / my_list_2[k]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            nList.append(division)
    return nList
