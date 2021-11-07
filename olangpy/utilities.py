from os import system


TESTS = []
def test(f):
    global TESTS
    TESTS.append(f)
    return f

def run_tests():
    global TESTS
    for i in TESTS:
        try:
            i()
        except AssertionError as e:
            system('clear')
            print('❌ TEST FAILED ❌')
            raise e
    system('clear')
    print(f'💪 {len(TESTS)} TESTS PASSED 💪')


# idea kinda stolen from Go
#   source: https://programming.guide/go/iota.html
# python has a built in enum.auto() that does the same
#   source: https://docs.python.org/3/library/enum.html#using-automatic-values
# but this is used intead because https://suckless.org/philosophy/

IOTA_COUNT = 0
def iota(reset: bool = False):
    global IOTA_COUNT
    IOTA_COUNT += 1
    if reset: IOTA_COUNT = 0
    return IOTA_COUNT

