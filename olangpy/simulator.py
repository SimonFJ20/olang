from typing import List
from parser import Op, OT
from utilities import test
from stack import Stack

def simulate(ops: List[Op], stack: Stack = Stack(), strings: List[str] = []):
    i = 0
    while i < len(ops):
        o = ops[i]
        if o.t == OT.PUSH_INT:
            stack.push(ops[i].v)
        elif o.t == OT.POP_INT:
            stack.pop()
        elif o.t == OT.PRINT_INT:
            v = stack.pop()
            print(v, end='', flush=True)
        elif o.t == OT.PUSH_STR:
            v = ops[i].v
            strings.append(v)
            stack.push(len(v))
            stack.push(len(strings) - 1)
        elif o.t == OT.POP_STR:
            stack.pop()
            stack.pop()
            strings.pop()
        elif o.t == OT.PRINT_STR:
            stack.pop()
            stack.pop()
            print(strings.pop(), end='', flush=True)  
        elif o.t == OT.DUP:
            v = stack.pop()
            stack.push(v)
            stack.push(v)
        elif o.t == OT.SWAP:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.push(v1)
            stack.push(v2)
        elif o.t == OT.OVER:
            a = stack.pop()
            b = stack.pop()
            stack.push(b)
            stack.push(a)
            stack.push(b)
        elif o.t == OT.ROT:
            a = stack.pop()
            b = stack.pop()
            c = stack.pop()
            stack.push(b)
            stack.push(a)
            stack.push(c)
        elif o.t == OT.ADD:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.push(v1 + v2)
        elif o.t == OT.SUB:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.push(v2 - v1)
        elif o.t == OT.IF:
            if not stack.pop():
                i = o.v
        elif o.t == OT.ELSE:
            i = o.v
        elif o.t == OT.WHILE:
            pass
        elif o.t == OT.DO:
            if not stack.pop():
                i = o.v
        elif o.t == OT.END:
            if o.v:
                i = o.v
        elif o.t == OT.CMP_EE:
            stack.push(1 if stack.pop() == stack.pop() else 0)
        elif o.t == OT.CMP_NE:
            stack.push(1 if stack.pop() != stack.pop() else 0)
        elif o.t == OT.CMP_LT:
            stack.push(1 if stack.pop() > stack.pop() else 0)
        elif o.t == OT.CMP_GT:
            stack.push(1 if stack.pop() < stack.pop() else 0)
        elif o.t == OT.CMP_LTE:
            stack.push(1 if stack.pop() >= stack.pop() else 0)
        elif o.t == OT.CMP_GTE:
            stack.push(1 if stack.pop() <= stack.pop() else 0)
        i += 1

@test
def it_should_have_pushed_value():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 5)], s)
    assert s.stack[0] == 5

@test
def it_should_do_calculation():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 3),
        Op(OT.PUSH_INT, 4),
        Op(OT.ADD)
    ], s);
    assert s.stack[0] == 7

@test
def it_should_do_calculation():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 3),
        Op(OT.PUSH_INT, 4),
        Op(OT.SUB)
    ], s);
    assert s.stack[0] == -1

@test
def it_should_handle_string_correctly():
    s = Stack()
    strings = []
    simulate([
        Op(OT.PUSH_STR, 'hello world')
    ], s, strings)
    assert s.stack[0] == 11
    assert s.stack[1] == 0
    assert strings[0] == 'hello world'

@test
def it_should_handle_string_popping_correctly():
    s = Stack()
    strings = []
    simulate([
        Op(OT.PUSH_STR, 'hello world'),
        Op(OT.POP_STR),
        Op(OT.PUSH_INT, 6)
    ], s, strings)
    assert s.stack[0] == 6


@test
def it_should_not_do_memory_leaky_leaky():
    s = Stack()
    strings = []
    simulate([
        Op(OT.PUSH_STR, 'hello world'),
        Op(OT.POP_STR),
    ], s, strings)
    assert len(strings) == 0

@test
def it_should_pop_pushed_values():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 7),
        Op(OT.POP_INT),  
        Op(OT.PUSH_INT, 8),
    ], s)
    assert s.pop() == 8

@test
def it_should_pop_when_printing_int():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 3),
        Op(OT.PUSH_INT, 7),
        Op(OT.PRINT_INT),
    ], s)
    assert s.pop() == 3

@test
def it_should_pop_when_printing_str():
    s = Stack()
    simulate([
        Op(OT.PUSH_STR, "ajf"),
        Op(OT.PUSH_STR, "lets goooooo"),
        Op(OT.PRINT_STR),
    ], s)
    assert s.pop() == 0 and s.pop() == 3

@test
def it_should_duplicate_value():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 5),
        Op(OT.DUP),
    ], s)
    assert s.pop() == 5 and s.pop() == 5

@test
def it_should_swap_the_two_top_values():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 5),
        Op(OT.PUSH_INT, 3),
        Op(OT.SWAP),
    ], s)
    assert s.pop() == 5 and s.pop() == 3

@test
def it_should_copy_2nc_item_to_top():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 5),
        Op(OT.PUSH_INT, 3),
        Op(OT.OVER),
    ], s)
    assert s.pop() == 5 and s.pop() == 3 and s.pop() == 5

@test
def it_should_move_3rd_item_to_top():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 4),
        Op(OT.PUSH_INT, 5),
        Op(OT.PUSH_INT, 6),
        Op(OT.ROT),
    ], s)
    assert s.pop() == 4

@test
def it_should_execute_if_correctly():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 1),
        Op(OT.IF, 3),
        Op(OT.PUSH_INT, 2),
        Op(OT.ELSE, 5),
        Op(OT.PUSH_INT, 3),
        Op(OT.END),
    ], s)
    assert s.pop() == 2

@test
def it_should_execute_if_correctly():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 0),
        Op(OT.IF, 3),
        Op(OT.PUSH_INT, 2),
        Op(OT.ELSE, 5),
        Op(OT.PUSH_INT, 3),
        Op(OT.END),
    ], s)
    assert s.pop() == 3

@test
def it_should_print_five_times():
    s = Stack()
    simulate([
        Op(OT.PUSH_INT, 5),
        Op(OT.WHILE),
        Op(OT.DUP),
        Op(OT.DO, 8),
        Op(OT.PUSH_STR, "should print five times\n"),
        Op(OT.PRINT_STR),
        Op(OT.PUSH_INT, 1),
        Op(OT.SUB),
        Op(OT.END, 1),
    ], s)
    assert s.pop() == 0

@test
def it_should_pop_two_and_push_one():
    correct = True
    for i in [OT.CMP_EE, OT.CMP_NE, OT.CMP_LT, OT.CMP_GT, OT.CMP_LTE, OT.CMP_GTE]:
        s = Stack()
        simulate([
            Op(OT.PUSH_INT, 69),
            Op(OT.PUSH_INT, 0),
            Op(OT.PUSH_INT, 1),
            Op(i),
        ], s)
        s.pop()
        if s.pop() != 69:
            correct = False
    assert correct

# ==

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_EE)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 8), Op(OT.CMP_EE)], s)
    assert s.pop() == 1

# !=

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 8), Op(OT.CMP_NE)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_NE)], s)
    assert s.pop() == 1

# <

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 4), Op(OT.CMP_LT)], s)
    assert s.pop() == 0

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 4), Op(OT.CMP_LT)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_LT)], s)
    assert s.pop() == 1

# >

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_GT)], s)
    assert s.pop() == 0

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 4), Op(OT.CMP_GT)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 4), Op(OT.CMP_GT)], s)
    assert s.pop() == 1

# <=

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 4), Op(OT.CMP_LTE)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 4), Op(OT.CMP_LTE)], s)
    assert s.pop() == 1

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_LTE)], s)
    assert s.pop() == 1

# >=

@test
def it_should_be_false():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 8), Op(OT.CMP_GTE)], s)
    assert s.pop() == 0

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 4), Op(OT.PUSH_INT, 4), Op(OT.CMP_GTE)], s)
    assert s.pop() == 1

@test
def it_should_be_true():
    s = Stack()
    simulate([Op(OT.PUSH_INT, 8), Op(OT.PUSH_INT, 4), Op(OT.CMP_GTE)], s)
    assert s.pop() == 1


