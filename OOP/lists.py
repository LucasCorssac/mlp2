# funções uteis para listas

empty = []


def first(one_list):
        return one_list[0]


def second(one_list):
    return one_list[1]


def rest(one_list):
    return one_list[1:]


def is_empty(one_list):
    if len(one_list) == 0:
        return True
    else:
        return False


def cons(element, one_list):
    if element != empty:
        aux_list = [element]
        return aux_list+one_list
    else:
        return []

