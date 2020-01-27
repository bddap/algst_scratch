#!/usr/bin/env python3
import itertools


def A(ls, fn, n):
    "for all n length tuples in ls, is predicate fn true"
    return all(fn(*tup) for tup in itertools.product(*(ls for _ in range(n))))


def magma(ls, op):
    # closure
    return A(ls, lambda a, b: op(a, b) in ls, 2)


def semigroup(ls, op):
    return (
        magma(ls, op)
        and  # associativity
        A(ls, lambda a, b, c: op(op(a, b), c) == op(a, op(b, c)), 3)
    )


def monoid(ls, op):
    return (
        semigroup(ls, op)
        and  # identity
        any(all(op(l, a) == a for a in ls) for l in ls)
    )


def group(ls, op):
    return (
        monoid(ls, op)
        and  # invertibility
        all(any(op(l, a) == l for a in ls) for l in ls)
    )


def ring(ls, op_add, op_mul):
    return (
        group(ls, op_add)
        and  # monoid under multiplication
        monoid(ls, op_mul)
        and  # multiplication is distributive with respect to addition
        A(ls, lambda a, b, c: (
            # left distributive
            op_mul(a, op_add(b, c)) == op_add(op_mul(a, b), op_mul(a, c))
            and  # right distributive
            op_mul(op_add(b, c), a) == op_add(op_mul(b, a), op_mul(c, a))
        ), 3)
    )


def frob():
    rank = 5
    se = set(range(rank))
    def op_add(a, b): return (a + b) % rank
    def op_mul(a, b): return (a * b) % rank

    assert magma(se, op_add)
    assert semigroup(se, op_add)
    assert monoid(se, op_add)
    assert group(se, op_add)
    assert ring(se, op_add, op_mul)


frob()
print("done")
