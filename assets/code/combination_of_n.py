#!/usr/bin python

def listed_binary(n):
    if n == 0:
        yield ""
    else:
        for bit in ('0', '1'):
            yield from (sbit+bit for sbit in listed_binary(n-1))


def masking(inp_set, str_bin):
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(inp_set, str_bin)))


def combination_of_n(inp_set, target):
    masks = list(listed_binary(len(inp_set)))
    for mask in masks:
        pick_set = list(masking(inp_set, mask))
        if len(pick_set) == target:
            yield pick_set

print(list(combination_of_n([1, 2, 3, 4, 5], 4)))