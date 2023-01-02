a = [1, 2, 3, 4, 5]

def permutations():
    global running
    global characters
    global bitmask

    if len(running) == len(characters):
        print(''.join(str(running)))
    else:
        for i in range(len(characters)):
            if ((bitmask >> i) & 1) == 0:
                bitmask |= 1 << i
                running.append(characters[i])
                permutations()
                bitmask ^= 1 << i  # make the bit zero again.
                running.pop()

characters = list(a)
running = []
bitmask = 0
permutations()