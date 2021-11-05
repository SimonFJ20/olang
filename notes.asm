

; hello world program

section .data
    s1 db "Hello world!",10
    s1_len equ $-s1

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, s1
    mov rdx, s1_len
    syscall

    mov rax, 60
    mov rdi, 0
    syscall



; print integer

    mov    eax, valuetoprint
    mov    ecx, 10        ;  digit count to generate
loop1:
    call   dividebyten
    add    eax, 0x30
    push   eax
    mov    eax, edx
    dec    ecx
    jne    loop1
    mov    ecx, 10        ;  digit count to print
loop2:   
    pop    eax
    call   printcharacter
    dec    ecx
    jne    loop2



