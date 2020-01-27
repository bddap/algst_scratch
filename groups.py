#!/usr/bin/env python3

from ops import BIN_PROPS as prop_tests
from ops import GROUP_CLASSES as classes
import common


def describe():
    mcn = max(len(cn) for cn, _ in classes)
    for cn, reqs in classes:
        needed = (pt.__name__ for req, pt in zip(reqs, prop_tests) if req)
        print(common.padto(cn, mcn), " & ".join(needed))
    print()


def frob(se, op):
    props = [pt(se, op) for pt in prop_tests]
    propnames = [pt.__name__ for pt in prop_tests]
    mpn = max(len(pn) for pn in propnames)

    print(f"Testing the set:\n{se}\nunder \"{op.__name__}\".")
    print()
    for pn, p in zip(propnames, props):
        print(common.padto(pn, mpn), p)
    print()

    mcn = max(len(cn) for cn, _ in classes)
    for classname, requirements in classes:
        is_classname = all(satisfied or not required for
                           satisfied, required in zip(props, requirements))
        print(common.padto(classname, mcn), is_classname)


def frobrank(rank):
    def add(a, b): return (a + b) % rank
    frob(set(range(rank)), add)


describe()
frobrank(12)
