format PE console                            ; 32-разрядная консольная программа WINDOWS EXE
entry start                                  ; точка входа

include 'include\win32a.inc'

section '.idata' import data readable        ; секция импортируемых функций

library kernel,'kernel32.dll',\
        msvcrt,'msvcrt.dll'

import  kernel,\
        ExitProcess,'ExitProcess'

import  msvcrt,\
        printf,'printf',\
        getchar,'_fgetchar'

section '.data' data readable writeable      ; секция данных

ARR dw 23,34,56,12,48,67,34,32,58,45         ; массив
MESSAGE	db "Result is %d",0                  ; текст сообщения

section '.code' code readable executable     ; секция кода

start:                                       ; точка входа в программу
		MOV EAX, -65000
		ADD EAX, 700
BEGIN_CYCLE:	XOR EAX,EAX	;беззнаковая конвертация
		MOV AX, [EBX]
		ADD EDX, EAX	;добавление текущего элемента массива
		ADD EBX, 2	;переход к следующему элементу массива
		LOOP BEGIN_CYCLE
	
		ccall [printf], MESSAGE, EDX
		ccall [getchar]
		stdcall [ExitProcess],0
