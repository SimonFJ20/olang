from utilities import test
from random import randint

class Stack():
    def __init__(self) -> None:
        self.stack = []
        self.index = -1

    def push(self, v: int):
        self.index += 1
        if self.index == len(self.stack):
            self.stack.append(v)
        else:
            self.stack[self.index] = v

    def pop(self) -> int:
        if self.index == -1:
            raise Exception("stack underflow")
        else:
            v = self.stack[self.index]
            self.index -= 1
            return v

@test
def it_should_return_value():
    s = Stack()
    s.push(69)
    assert s.pop() == 69

@test
def it_should_raise_stack_underflow():
    s = Stack()
    s.push(5)
    s.pop()
    try:
        s.pop()
        assert False, 'didnt throw'
    except Exception as e:
        assert not isinstance(e, AssertionError)

@test
def it_should_return_both_values_in_order():
    s = Stack()
    a = 4
    b = 32254
    s.push(a)
    s.push(b)
    assert s.pop() == b and s.pop() == a

@test
def it_should_just_work():
    s = Stack()
    values = []
    for i in range(randint(0, 100)):
        values.append(randint(-10000, 10000))
    for v in values:
        s.push(v)
    i = len(values) - 1
    correct = True
    while i >= 0:
        if s.pop() != values[i]:
            correct = False
            break
        i -= 1
    assert correct
    
@test
def it_should_pop_right_values():
    s = Stack()
    s.push(5)
    s.pop()
    s.push(38)
    assert s.pop() == 38
