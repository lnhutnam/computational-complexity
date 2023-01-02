#!/usr/bin python

# use a binary number (represented as string) as a mask
def mask(lst, m):
    # pad number to create a valid selection mask
    # according to definition in the solution laid out
    m = m.zfill(len(lst))
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))


def ssp(lst, target):
    # there are 2^n binary numbers with length of the original list
    for i in range(2**len(lst)):
        # create the pick corresponsing to current number
        pick = list(mask(lst, bin(i)[2:]))
        if sum(pick) == target:
            yield pick


# use 'list' to unpack the generator
print(list(ssp([1, 2, 3, 4, 5], 7)))


def inclusion_exclusion_ssp(inp_set, target):
    if len(inp_set) == 0:
        return target == 0
    else:
        first_element = inp_set[0]
        rest = inp_set[1:]
        return inclusion_exclusion_ssp(rest, target) or inclusion_exclusion_ssp(rest, target - first_element)


print((inclusion_exclusion_ssp([1, 2, 3, 4, 5], 7)))


def listed_binary(n):
    if n == 0:
        yield ""
    else:
        for bit in ('0', '1'):
            yield from (sbit+bit for sbit in listed_binary(n-1))


def masking(inp_set, str_bin):
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(inp_set, str_bin)))


def ssp(inp_set, target):
    masks = list(listed_binary(len(inp_set)))
    for mask in masks:
        pick_set = list(masking(inp_set, mask))
        if sum(pick_set) == target:
            yield pick_set

print(list(ssp([1, 2, 3, 4, 5], 7)))
