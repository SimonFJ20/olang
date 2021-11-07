from sys import argv
from crosrefs import cross_reference
from parser import parse
from utilities import run_tests
from simulator import simulate
from lexer import chop_words


if __name__ == '__main__':
    assert len(argv) <= 2, "nej noo"
    if argv[1] == 'test':
        run_tests()
        exit(0)
    with open(argv[1]) as f:
        program = f.read()
        f.close()
        words = chop_words(program)
        ops = parse(words)
        cross_reference(ops)
        simulate(ops)

