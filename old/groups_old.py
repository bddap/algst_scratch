#!/usr/bin/env python3


def inc_through_group(p, start):
    for i in range(1, p + 1):
        yield (start * i) % p


for group in range(8):
    for i in range(group):
        print(list(inc_through_group(group, i)))
