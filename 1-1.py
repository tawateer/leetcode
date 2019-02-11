#!/bin/env python


def f(source, target):
    length = len(source)

    m = {}
    for i in xrange(length):
        m[source[i]] = i

    for i in xrange(length):
        search = target - source[i]

        value = m.get(search, None)
        if value is not None:
            return i, value
    return None, None


print f([2, 7, 11, 15], 9)
