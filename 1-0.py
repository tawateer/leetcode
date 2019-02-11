#!/bin/env python


def f(source, target):
    length = len(source)
    for i in xrange(length):
        j = i + 1
        if j < length:
            if source[i] + source[j] == target:
                return i, j
            j += 1
    return None, None


print f([2, 7, 11, 15], 9)
