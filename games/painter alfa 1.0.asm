IDEAL
MODEL small
STACK 100h
DATASEG
; --------------------------
sizx dw 5
; --------------------------
CODESEG

proc pr
	

	ret
endp pr

start:
	mov ax, @data
	mov ds, ax
; --------------------------
	mov ah, 00h
	mov al, 4h
	int 10h
	
	mov ax, 0h
	int 33h
	
	mov ax, 1h
	int 33h
	
	mov cx, 10
looper:
	push cx
	mov ax, 0003h
	int 33h
	;x = cx
	; y = dx
	xor bx, bx
	mov ah, 0ch; interrupt
	mov al, 0fh; color
	mov bh, 00h; page
	int 10h
	pop cx
	inc cx
loop looper
	
; --------------------------


	
exit:
	mov ax, 4c00h
	int 21h
END start


