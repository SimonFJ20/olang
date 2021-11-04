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


IOTA_COUNT = 0
def iota(reset: bool = False):
    global IOTA_COUNT
    IOTA_COUNT += 1
    if reset: IOTA_COUNT = 0
    return IOTA_COUNT

