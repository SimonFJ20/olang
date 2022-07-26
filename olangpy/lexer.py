from typing import List
from utilities import test

def chop_words(text: str) -> List[str]:
    words: List[str] = []
    word = ''
    is_string = False
    was_string = False
    for c in text:
        if c in ' \t\n' and not is_string:
            if word != '':
                words.append(word)
                word = ''
                was_string = False
        else:
            if c == '"':
                if is_string:
                    was_string = True
                is_string = not is_string
            elif was_string:
                raise Exception()
            word += c
    if is_string:
        raise Exception()
    if word != '':
        words.append(word)
    return words
    

@test
def it_should_return_empty_list():
    assert chop_words('') == []

@test
def it_should_return_word():
    assert chop_words('hello') == ['hello']

@test
def it_should_empty_list():
    assert chop_words('  ') == []

@test
def it_should_return_words_split():
    assert chop_words('hello world') == ['hello', 'world']

@test
def it_should_conserve_strings():
    assert chop_words('"hello world"') == ['"hello world"']

@test
def it_should_chop_words_beside_strings():
    i = 'pop "hello world" print'
    o = ['pop', '"hello world"',  'print']
    assert chop_words(i) == o

@test
def it_should_treat_multiple_spaces_as_single_space():
    i = 'pop       print'
    o = ['pop', 'print']
    assert chop_words(i) == o

@test
def it_should_treat_all_whitespace_as_single_space():
    i = 'pop   \t \n\n  print\n'
    o = ['pop', 'print']
    assert chop_words(i) == o

@test
def it_should_treat_tab_and_newline_as_space_beside_string():
    i = '\t"hell wrld"\n'
    o = ['"hell wrld"']
    assert chop_words(i) == o

@test
def it_should_chop_newline_and_tab_seperated_words():
    i = '\tpush\npop'
    o = ['push', 'pop']
    assert chop_words(i) == o

@test
def it_should_complain_about_syntax1():
    try:
        chop_words('dsa"my string"sd')
        assert False, "didnt throw"
    except Exception as e:
        assert not isinstance(e, AssertionError)

@test
def it_should_complain_about_syntax2():
    try:
        chop_words('"my str')
        assert False, "didnt throw"
    except Exception as e:
        assert not isinstance(e, AssertionError)

@test
def it_should_conserve_whitespace_in_strings():
    i = '"\ttabbed in\non new line"'
    o = ['"\ttabbed in\non new line"']
    assert chop_words(i) == o

