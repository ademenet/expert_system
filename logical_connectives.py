"""
Logical connectives implementations.
"""

def logical_and(left: bool, right: bool) -> bool:
    return left & right

def logical_or(left: bool, right: bool) -> bool:
    return left | right

def logical_xor(left: bool, right: bool) -> bool:
    return left ^ right

def logical_neg(left: bool) -> bool:
    return not left
