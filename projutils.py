


from os import system


TESTS = []
def test(f):
    global TESTS
    TESTS.append(f)
    return f

def run_tests():
    global TESTS
    for i in TESTS:
        i()
    system('clear')
    print('\n\nall tests passed')

IOTA_COUNT = 0
def iota(reset: bool = False):
    global IOTA_COUNT
    IOTA_COUNT += 1
    if reset: IOTA_COUNT = 0
    return IOTA_COUNT

