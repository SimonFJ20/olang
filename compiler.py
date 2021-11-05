from typing import List
from op_maker import Op, OT
from subprocess import call
from os import remove

header = '''
default rel
extern printf
section .rodata
    format db "%#x", 10, 0
'''

subroutines = '''
section .text
    global olang_print_int

olang_print_int:
    sub rsp, 8
    mov esi, 0x12345678
    lea rdi, [rel format]
    xor eax, eax
    call printf
    xor eax, eax
    add rsp, 8
    ret

'''

def get_strings(ops: List[Op]) -> List[str]:
    strings: List[str] = []
    for i in ops:
        if i.t == OT.PUSH_STR:
            strings.append(i.v)
    return strings

def compile(ops: List[Op]):
    asm = header
    strings = get_strings(ops)
    asm += 'section .data\n'
    for i in range(len(strings)):
        asm += f'    s{i} db {strings[i]}\n'
        asm += f'    s{i}l equ $-s{i}\n'
    
    asm += subroutines
    asm += '\nsection .text\n    global _start\n\n'

    depth = 0
    for o in ops:
        if o.t == OT.PUSH_INT:
            asm += f'    ; PUSH_INT\n'
            asm += f'    mov rax, {o.v}\n'
            asm += f'    push rax\n'
        elif o.t == OT.POP_INT:
            asm += f'    ; POP_INT\n'
            asm += f'    pop rax\n'
        elif o.t == OT.PRINT_INT:
            asm += f'    ; PRINT_INT\n'
            asm += f'    call olang_print_int\n'
        elif o.t == OT.PUSH_STR:
            assert False, 'not implemented'
        elif o.t == OT.POP_STR:
            assert False, 'not implemented'
        elif o.t == OT.PRINT_STR:
            assert False, 'not implemented'
        elif o.t == OT.DUP:
            assert False, 'not implemented'
        elif o.t == OT.SWAP:
            assert False, 'not implemented'
        elif o.t == OT.ADD:
            assert False, 'not implemented'
        elif o.t == OT.SUB:
            assert False, 'not implemented'
        elif o.t == OT.IF:
            assert False, 'not implemented'
        elif o.t == OT.ELSE:
            assert False, 'not implemented'
        elif o.t == OT.WHILE:
            assert False, 'not implemented'
        elif o.t == OT.DO:
            assert False, 'not implemented'
        elif o.t == OT.END:
            assert False, 'not implemented'
        elif o.t == OT.CMP_EE:
            assert False, 'not implemented'
        elif o.t == OT.CMP_NE:
            assert False, 'not implemented'
        elif o.t == OT.CMP_LT:
            assert False, 'not implemented'
        elif o.t == OT.CMP_GT:
            assert False, 'not implemented'
        elif o.t == OT.CMP_LTE:
            assert False, 'not implemented'
        elif o.t == OT.CMP_GTE:
            assert False, 'not implemented'

    asm += '    mov rax, 60\n'
    asm += '    mov rdi, 0\n'
    asm += '    syscall\n'

    with open('temp.asm', 'w') as f:
        f.write(asm)
        f.close()
    # call(['nasm', '-f', 'elf64', '-o', 'temp.o', 'temp.asm'])
    # remove('temp.asm')
    # call(['ld', '-o', 'a.out', 'temp.o'])
    # remove('temp.o')

