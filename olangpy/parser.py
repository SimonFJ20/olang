from typing import List
from utilities import iota, test
from enum import Enum
from re import match
import random

class OT(Enum):
    PUSH_INT    = iota(True)# 67 -3 0
    POP_INT     = iota()    # pop_int
    PRINT_INT   = iota()    # print_int
    PUSH_STR    = iota()    # "hello world!"
    POP_STR     = iota()    # pop_str
    PRINT_STR   = iota()    # print_str
    DUP         = iota()    # dup
    SWAP        = iota()    # swap
    OVER        = iota()    # over
    ROT         = iota()    # rot
    ADD         = iota()    # +
    SUB         = iota()    # -
    MUL         = iota()    # *
    DIV         = iota()    # /
    MOD         = iota()    # %
    IF          = iota()    # if
    ELSE        = iota()    # else
    WHILE       = iota()    # while
    DO          = iota()    # do
    END         = iota()    # end
    PROC        = iota()    # proc
    RETURN      = iota()    # return
    CMP_EE      = iota()    # ==
    CMP_NE      = iota()    # !=
    CMP_LT      = iota()    # <
    CMP_GT      = iota()    # >
    CMP_LTE     = iota()    # <=
    CMP_GTE     = iota()    # >=
    CALL        = iota()    # >=

class Op:
    def __init__(self, t: OT, v = None):
        self.t = t
        self.v = v

def parse(words: List[str]) -> List[Op]:
    ops: List[Op] = []
    for w in words:
        if match('^\-?\d+$', w):
            ops.append(Op(OT.PUSH_INT, int(w)))
        elif w == 'pop_int':
            ops.append(Op(OT.POP_INT))
        elif w == 'print_int':
            ops.append(Op(OT.PRINT_INT))
        elif w.startswith('"') and w.endswith('"'):
            w = w.replace('\\n', '\n', -1)
            w = w.replace('\\t', '\t', -1)
            w = w.replace('\\"', '"', -1)
            ops.append(Op(OT.PUSH_STR, w[1:-1]))
        elif w == 'pop_str':
            ops.append(Op(OT.POP_STR))
        elif w == 'print_str':
            ops.append(Op(OT.PRINT_STR))
        elif w == 'dup':
            ops.append(Op(OT.DUP))
        elif w == 'swap':
            ops.append(Op(OT.SWAP))
        elif w == 'over':
            ops.append(Op(OT.OVER))
        elif w == 'rot':
            ops.append(Op(OT.ROT))
        elif w == '+':
            ops.append(Op(OT.ADD))
        elif w == '-':
            ops.append(Op(OT.SUB))
        elif w == '*':
            ops.append(Op(OT.MUL))
        elif w == '/':
            ops.append(Op(OT.DIV))
        elif w == '%':
            ops.append(Op(OT.MOD))
        elif w == 'if':
            ops.append(Op(OT.IF))
        elif w == 'else':
            ops.append(Op(OT.ELSE))
        elif w == 'while':
            ops.append(Op(OT.WHILE))
        elif w == 'do':
            ops.append(Op(OT.DO))
        elif w == 'proc':
            ops.append(Op(OT.PROC))
        elif w == 'end':
            ops.append(Op(OT.END))
        elif w == '==':
            ops.append(Op(OT.CMP_EE))
        elif w == '!=':
            ops.append(Op(OT.CMP_NE))
        elif w == '<':
            ops.append(Op(OT.CMP_LT))
        elif w == '>':
            ops.append(Op(OT.CMP_GT))
        elif w == '<=':
            ops.append(Op(OT.CMP_LTE))
        elif w == '>=':
            ops.append(Op(OT.CMP_GTE))
        else:
            ops.append(Op(OT.CALL, w))
    return ops




@test
def should_return_add():
    i = ["+"]
    res = parse(i)
    assert res[0].t == OT.ADD

@test
def should_be_same_length():
    l = int(random.random() * 100)
    i = ['+']*l
    res = parse(i)
    assert len(res) == l

@test
def should_return_sub():
    i = ['-']
    res = parse(i)
    assert res[0].t == OT.SUB

@test
def should_return_mul():
    i = ['*']
    res = parse(i)
    assert res[0].t == OT.MUL

@test
def should_return_div():
    i = ['/']
    res = parse(i)
    assert res[0].t == OT.DIV

@test
def should_return_mod():
    i = ['%']
    res = parse(i)
    assert res[0].t == OT.MOD

@test
def should_NOT_just_return_add():
    res = parse(["5", "20", "+"])
    assert (res[0].v == 5 and res[1].v == 20 and res[2].t == OT.ADD)

@test
def should_allow_escaped_strings():
    res = parse(['"h\\"abc fuck dig"'])
    assert res[0].v == 'h"abc fuck dig'

@test
def should_allow_for_negative_numbers():
    assert parse(['-3'])[0].v == -3

@test
def should_replace_escaped_chars():
    assert parse(['"\\n"'])[0].v == "\n"
    assert parse(['"\\t"'])[0].v == "\t"

@test
def should_return_if_op():
    assert parse(['if'])[0].t == OT.IF

@test
def should_return_else_op():
    assert parse(['else'])[0].t == OT.ELSE

@test
def should_return_while_op():
    assert parse(['while'])[0].t == OT.WHILE

@test
def should_return_do_op():
    assert parse(['do'])[0].t == OT.DO

@test
def should_return_proc_op():
    assert parse(['proc'])[0].t == OT.PROC

@test
def should_return_end_op():
    assert parse(['end'])[0].t == OT.END

@test
def should_return_e_op():
    assert parse(['=='])[0].t == OT.CMP_EE

@test
def should_return_ne_op():
    assert parse(['!='])[0].t == OT.CMP_NE

@test
def should_return_lt_op():
    assert parse(['<'])[0].t == OT.CMP_LT

@test
def should_return_gt_op():
    assert parse(['>'])[0].t == OT.CMP_GT

@test
def should_return_lte_op():
    assert parse(['<='])[0].t == OT.CMP_LTE

@test
def should_return_gte_op():
    assert parse(['>='])[0].t == OT.CMP_GTE

@test
def should_return_call_op():
    assert parse(['something_that_isn\'t_an_operation'])[0].t == OT.CALL

@test
def should_return_callee_name():
    assert parse(['called_proc'])[0].v == "called_proc"


