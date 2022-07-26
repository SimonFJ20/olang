from typing import List, Optional
from parser import OT, Op
from utilities import test


def cross_forward_refernces(ops: List[Op]) -> None:
    stack: List[Optional[int]] = []
    for i in range(len(ops)):
        if ops[i].t == OT.IF:
            stack.append(None)
        elif ops[i].t == OT.WHILE:
            stack.append(i)
        elif ops[i].t == OT.PROC:
            stack.append(i)
        elif ops[i].t == OT.END:
            ops[i].v = stack.pop()

def cross_backward_refernces(ops: List[Op]) -> None:
    stack = []
    for i in reversed(range(len(ops))):
        if ops[i].t == OT.END:
            stack.append(i)
        elif ops[i].t in [OT.IF, OT.DO]:
            ops[i].v = stack.pop()
        elif ops[i].t == OT.ELSE:
            ops[i].v = stack.pop()
            stack.append(i)
        elif ops[i].t == OT.PROC:
            ops[i].v = stack.pop()

def cross_reference(ops: List[Op]) -> None:
    cross_forward_refernces(ops)
    cross_backward_refernces(ops)

@test
def it_should_not_cross_ref_if_end():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.IF),
        Op(OT.PUSH_INT, 1),
        Op(OT.WHILE),
        Op(OT.DUP),
        Op(OT.DO),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[-1].v == None

@test
def it_should_cross_ref_while_end():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.IF),
        Op(OT.PUSH_INT, 1),
        Op(OT.WHILE),
        Op(OT.DUP),
        Op(OT.DO),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[-2].v == 3

@test
def it_should_cross_ref_if_to_end():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.IF),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[1].v == 4

@test
def it_should_cross_ref_if_to_else():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.IF),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.ELSE),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[1].v == 4

@test
def it_should_cross_ref_else_to_end():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.IF),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.ELSE),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[4].v == 7

@test
def it_should_cross_ref_do_to_end():
    ops: List[Op] = [
        Op(OT.PUSH_INT, 1),
        Op(OT.WHILE),
        Op(OT.DUP),
        Op(OT.DO),
        Op(OT.PUSH_STR, "hello"),
        Op(OT.PRINT_STR),
        Op(OT.END),
    ]
    cross_reference(ops)
    assert ops[3].v == 6
