IDEAL
MODEL small
STACK 100h
P386
DATASEG
; --------------------------
color db ?
painterX dw -30h
painterY dw 190h
; --------------------------
CODESEG
proc XorAll
	xor ax, ax
	xor bx, bx
	xor cx, cx
	xor dx, dx
	ret
endp XorAll
proc paintGREEN
	mov cx, 10
raw:
	push cx
	mov ah, 0ch
	mov al, 02h
	mov bh, 00h
	mov cx, [painterX]
	mov dx, [painterY]
	int 10h
	pop cx
	inc [painterX]
	loop raw
	ret
endp paintGREEN
start:
    mov ax, @data
    mov ds, ax
;--------------------------- set up
    mov ax, 13h
    int 10h
	mov ax, 0h
	int 33h
	
	mov ax, 1h
	int 33h
	mov [color], 0000fh
	
;--------------------------- set up background

;---------------------------

mloop:
    mov ax, 3
    int 33h
    cmp bx, 1
    jne mloop
    push dx
    mov ax, cx
    xor dx, dx
    mov bx, 2
    div bx
    mov cx, ax
    pop dx
    xor bx, bx
    mov ah, 0ch; interrupt
    mov al, [color]; color
    mov bh, 00h; page
    int 10h
    jmp mloop 
;---------------------------

exit:
    mov ax, 4c00h
    int 21h
END start