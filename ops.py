import itertools


def A(ls, fn, n):
    "for all n length tuples in ls, is predicate fn true"
    return all(fn(*tup) for tup in itertools.product(*(ls for _ in range(n))))


def totality(ls, op):
    # equvalent to closure
    return A(ls, lambda a, b: op(a, b) in ls, 2)


def associativity(ls, op):
    return A(ls, lambda a, b, c: op(op(a, b), c) == op(a, op(b, c)), 3)


def identity(ls, op):
    return any(all(op(l, a) == a for a in ls) for l in ls)


def invertibility(ls, op):
    return all(any(op(l, a) == l for a in ls) for l in ls)


def commutativity(ls, op):
    return A(ls, lambda a, b: op(a, b) == op(b, a), 2)


def annihilate(ls, op):
    "there exists an annihilating element in ls under op"
    return any(all(op(a, b) == a for b in ls) for a in ls)


BIN_PROPS = [totality, associativity, identity, invertibility, commutativity,
             annihilate]

semigroupoid = [False, True, False, False, False, False]
small_category = [False, True, True, False, False, False]
groupoid = [False, True, True, True, False, False]
magma = [True, False, False, False, False, False]
quasigroup = [True, False, False, True, False, False]
unital_magma = [True, False, True, False, False, False]
loop = [True, False, True, True, False, False]
semigroup = [True, True, False, False, False, False]
inverse_semigroup = [True, True, False, True, False, False]
monoid = [True, True, True, False, False, False]
commutative_monoid = [True, True, True, False, True, False]
group = [True, True, True, True, False, False]
abelian_group = [True, True, True, True, True, False]

GROUP_CLASSES = [
    ["semigroupoid", semigroupoid],
    ["small_category", small_category],
    ["groupoid", groupoid],
    ["magma", magma],
    ["quasigroup", quasigroup],
    ["unital_magma", unital_magma],
    ["loop", loop],
    ["semigroup", semigroup],
    ["inverse_semigroup", inverse_semigroup],
    ["monoid", monoid],
    ["commutative_monoid", commutative_monoid],
    ["group", group],
    ["abelian_group", abelian_group],
]


def property_satisfactions(ls, op):
    return [bp(ls, op) for bp in BIN_PROPS]


def satisfies(satisfactions, requirements):
    return all(satisfied or not required for
        satisfied, required in zip(satisfactions, requirements))


def distributivity(ls, opa, opb):
    return A(ls, lambda a, b, c: (
        opb(a, opa(b, c)) == opa(opb(a, b), opb(a, c))
        and
        opb(opa(a, b), c) == opa(opb(a, c), opb(b, c))
    ), 3)
