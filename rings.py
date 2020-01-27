#!/usr/bin/env python3

import ops


def is_ring(ls, op_add, op_mul):
    ab_group = ops.satisfies(ops.property_satisfactions(ls, op_add),
                             ops.abelian_group)
    monoid = ops.satisfies(ops.property_satisfactions(ls, op_mul),
                           ops.monoid)
    distributive = ops.distributivity(ls, op_add, op_mul)
    return ab_group and monoid and distributive


def frob():
    rank = 11
    R = set(range(rank))
    def op_add(a, b): return (a + b) % rank
    def op_mul(a, b): return (a * b) % rank
    ring = is_ring(R, op_add, op_mul)
    print(f"R: {R}\nis_ring: {ring}")


frob()
